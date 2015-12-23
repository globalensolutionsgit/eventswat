from __future__ import unicode_literals
from events.models import *
import logging
import pyelasticsearch
import requests
from django.utils.html import strip_tags
from haystack.utils import Highlighter
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine, ElasticsearchSearchBackend, ElasticsearchSearchQuery
from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import EmptySearchQuerySet
from haystack.indexes import *
from templated_email.backends.vanilla_django import TemplateBackend
from django.conf import settings
from django.template import Context, TemplateDoesNotExist
from django.template.loader import get_template
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import EmptySearchQuerySet

RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 10)
print 'RESULTS_PER_PAGE', RESULTS_PER_PAGE

class Highlighter(object):
    css_class = 'highlighted'
    html_tag = 'span'
    max_length = 200
    text_block = ''
    
    def __init__(self, query, **kwargs):
        self.query = query
        
        if 'max_length' in kwargs:
            self.max_length = int(kwargs['max_length'])
        
        if 'html_tag' in kwargs:
            self.html_tag = kwargs['html_tag']
        
        if 'css_class' in kwargs:
            self.css_class = kwargs['css_class']
        
        self.query_words = set([word.lower() for word in self.query.split() if not word.startswith('-')])
    
    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        
        start_offset, end_offset = self.find_window(highlight_locations)
 
        
        return self.render_html(highlight_locations, start_offset, end_offset)
    
    def find_highlightable_words(self):
        # Use a set so we only do this once per unique word.
        word_positions = {}
        
        # Pre-compute the length.
        end_offset = len(self.text_block)
        lower_text_block = self.text_block.lower()
        
        for word in self.query_words:
            if not word in word_positions:
                word_positions[word] = []
            
            start_offset = 0
            
            while start_offset < end_offset:
                next_offset = lower_text_block.find(word, start_offset, end_offset)
                
                # If we get a -1 out of find, it wasn't found. Bomb out and
                # start the next word.
                if next_offset == -1:
                    break
                
                word_positions[word].append(next_offset)
                start_offset = next_offset + len(word)
      
        return word_positions
    
    def find_window(self, highlight_locations):
        best_start = 0
        best_end = self.max_length
        
        # First, make sure we have words.
        if not len(highlight_locations):
            return (best_start, best_end)
        
        words_found = []
        
        # Next, make sure we found any words at all.
        for word, offset_list in highlight_locations.items():
            if len(offset_list):
                # Add all of the locations to the list.
                words_found.extend(offset_list)
        
        if not len(words_found):
            return (best_start, best_end)
        
        if len(words_found) == 1:
            return (words_found[0], words_found[0] + self.max_length)
        
        # Sort the list so it's in ascending order.
        words_found = sorted(words_found)
        
        # We now have a denormalized list of all positions were a word was
        # found. We'll iterate through and find the densest window we can by
        # counting the number of found offsets (-1 to fit in the window).
        highest_density = 0
        best_start_new=0
        if words_found[:-1][0] > self.max_length:
            best_start = words_found[:-1][0]
            best_start_new=best_start
            best_end = best_start + self.max_length
        
        for count, start in enumerate(words_found[:-1]):
            current_density = 1
            
            for end in words_found[count + 1:]:
                if end - start < self.max_length:
                    current_density += 1
                else:
                    current_density = 0
                
                # Only replace if we have a bigger (not equal density) so we
                # give deference to windows earlier in the document.
                if current_density > highest_density:
                    best_start = best_start_new
                    best_end = start + self.max_length
                    # highest_density = current_density
        
        return (best_start, best_end)
    
    def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
        # Start by chopping the block down to the proper window.
        text = self.text_block
        start_offset = 0
        remaining_text=text
        # Invert highlight_locations to a location -> term list
        term_list = []
        
        for term, locations in highlight_locations.items():
            term_list += [(loc - start_offset, term) for loc in locations]
         
        loc_to_term = sorted(term_list)
        
        # Prepare the highlight template
        if self.css_class:
            hl_start = '<%s class="%s">' % (self.html_tag, self.css_class)
        else:
            hl_start = '<%s>' % (self.html_tag)
        
        hl_end = '</%s>' % self.html_tag
        highlight_length = len(hl_start + hl_end)
        
        # Copy the part from the start of the string to the first match,
        # and there replace the match with a highlighted version.
        highlighted_chunk = ""
        matched_so_far = 0
        prev = 0
        prev_str = ""
        for cur, cur_str in loc_to_term:
            if cur > len(text)-len(remaining_text) or len(text)-len(remaining_text) == 0:
                
                # This can be in a different case than cur_str
                actual_term = text[cur:cur + len(cur_str)]
                remaining_text=text[cur+len(cur_str):len(text)]
                
                # Handle incorrect highlight_locations by first checking for the term
           
                if actual_term.lower() == cur_str:
               
                    highlighted_chunk += text[prev + len(prev_str):cur] + hl_start + actual_term + hl_end
                    prev = cur
                    prev_str = cur_str
                
                    # Keep track of how far we've copied so far, for the last step
                    matched_so_far = cur + len(actual_term)
                
        # Don't forget the chunk after the last term
        highlighted_chunk += text[matched_so_far:]
        
        if start_offset > 0:
            rem_text = self.text_block[0:start_offset]
            highlighted_chunk = '%s' % highlighted_chunk
 
            #highlighted_chunk = '...%s' % highlighted_chunk
        
        if end_offset < len(self.text_block):
            highlighted_chunk = '%s' % highlighted_chunk
        
        return highlighted_chunk


class SearchHighlighter(Highlighter):
  max_length = 3600

  def highlight(self, text_block):
    output = super(SearchHighlighter, self).highlight(text_block)
    return output

class EventSearchBackend(ElasticsearchSearchBackend):

  def build_search_kwargs(self, *args, **kwargs):

    # # Uncomment following lines to see actual queries
    # log = logging.getLogger('pyelasticsearch')
    # stream = logging.StreamHandler()
    # stream.setLevel(logging.DEBUG)
    # log.setLevel(logging.DEBUG)
    # log.addHandler(stream)

    o = super(EventSearchBackend, self).build_search_kwargs(*args, **kwargs)
    if hasattr(self, 'default_operator'):
      q = o['query']['filtered']['query']
      if 'query_string' in q:
        q['query_string']['default_operator'] = self.default_operator

    return o  

  def percolator(self, uid, doc, params=None):
    try:    
      raw_results = self.conn.index(
        '_percolator', self.index_name, doc, id=uid)
    except (requests.RequestException, pyelasticsearch.ElasticHttpError) as e:
      if not self.silently_fail:
          raise
      self.log.error("Failed to query Elasticsearch using '%s': %s for %s", uid, e, doc)
      raw_results = {'ok': False}

    return raw_results['ok']

  def percolate(self, index, doc, params=None):
    prepped_data = index().full_prepare(doc)
    final_data = {}
    for key, value in prepped_data.items():
      final_data[key] = self._from_python(value)

    final_data = {'doc': final_data}    
    try:
      raw_results = self.conn.percolate(self.index_name, 'modelresult',
        final_data)
    except (requests.RequestException, pyelasticsearch.ElasticHttpError) as e:
      if not self.silently_fail:
          raise
      self.log.error("Failed to query Elasticsearch using '%s': %s", 
        self.index_name, e)
      raw_results = {}

    return raw_results   

class EventSearchQuery(ElasticsearchSearchQuery):
  
  def get_raw_query(self, spelling_query=None, **kwargs):
    query_string = self.build_query()
    _kwargs = self.build_params(spelling_query, **kwargs)
    # results = self.backend.search(query_string, **_kwargs)    

    if not self.backend.setup_complete:
      self.backend.setup()

    search_kwargs = self.backend.build_search_kwargs(query_string, **_kwargs)
    search_kwargs['from'] = _kwargs.get('start_offset', 0)

    order_fields = set()
    for order in search_kwargs.get('sort', []):
      for key in order.keys():
        order_fields.add(key)

    # geo_sort = '_geo_distance' in order_fields

    end_offset = _kwargs.get('end_offset')
    start_offset = _kwargs.get('start_offset', 0)
    if end_offset is not None and end_offset > start_offset:
      search_kwargs['size'] = end_offset - start_offset


    return search_kwargs


  def percolator(self, uid, params=None, **kwargs):
    search_kwargs = self.get_raw_query(**kwargs)
    return self.backend.percolator(uid, search_kwargs, params)

  def percolate(self, index, doc, params=None):
    return self.backend.percolate(index, doc, params)


class EventSearchEngine(ElasticsearchSearchEngine):
  backend = EventSearchBackend
  query = EventSearchQuery


class SearchView(object):
    print 'SearchView in Search_sites'
    template = 'search/search.html'
    extra_context = {}
    query = ''
    results = EmptySearchQuerySet()
    request = None
    form = None
    results_per_page = RESULTS_PER_PAGE
    print 'results_per_page', results_per_page

    def __init__(self, template=None, load_all=True, form_class=None, searchqueryset=None, context_class=RequestContext, results_per_page=None):
        print 'SearchView in __init__'
        print 'results_per_page with __init__', results_per_page        
        self.load_all = load_all
        self.form_class = form_class
        self.context_class = context_class
        self.searchqueryset = searchqueryset
        print 'self.searchqueryset', self.searchqueryset

        if form_class is None:
            self.form_class = ModelSearchForm

        if not results_per_page is None:
            print 'results_per_page with condition', results_per_page
            self.results_per_page = results_per_page
            print 'self.results_per_page', self.results_per_page

        if template:
            self.template = template

    def __call__(self, request):        
        print 'SearchView in Search_sites_call()'

        """
        Generates the actual response to the search.

        Relies on internal, overridable methods to construct the response.
        """
        self.request = request

        self.form = self.build_form()
        self.query = self.get_query()
        self.results = self.get_results()

        return self.create_response()

    def build_form(self, form_kwargs=None):

        print 'SearchView in build_form()'
        """
        Instantiates the form the class should use to process the search query.
        """
        data = None
        kwargs = {
            'load_all': self.load_all,
        }
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.GET):
            data = self.request.GET

        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = self.searchqueryset

        return self.form_class(data, **kwargs)

    def get_query(self):

        print 'SearchView in get_query()'
        """
        Returns the query provided by the user.

        Returns an empty string if the query is invalid.
        """
        if self.form.is_valid():
            return self.form.cleaned_data['q']

        return ''

    def get_results(self):
        print 'get_results'    
        """
        Fetches the results via the form.

        Returns an empty list if there's no query to search with.
        """
        return self.form.search()

    def build_page(self):
        print 'build_page' 
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
       
       
        if self.request.GET.get('page'):
            print 'self.request.GET.get(page)', self.request.GET.get('page')
            page_no = self.request.GET.get('page')
            if page_no > 1 :
                page_no = int(self.request.GET.get('page'))
                print 'page_no', page_no
            else:
                page_no = 1
        else:
            page_no = 1
            
      
        if self.request.GET.get('result_per_page'):
            print 'get result per page condition'
            result_display = self.request.GET.get('result_per_page')
            if result_display >  1 :
                result_display = int(self.request.GET.get('result_per_page'))
                print 'result_display', result_display
            else:
                result_display = RESULTS_PER_PAGE 
        else:
            result_display = RESULTS_PER_PAGE

        
        start_offset = (page_no - 1) * result_display
        self.results[start_offset:start_offset + result_display]

        paginator = Paginator(self.results, result_display)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)

    def extra_context(self):
        print 'build_page in extra_context'
        """
        Allows the addition of more context variables as needed.

        Must return a dictionary.
        """
        return {}

    def create_response(self):
        print 'Create response'
        """
        Generates the actual HttpResponse to send back to the user.
        """
        (paginator, page) = self.build_page()

        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'paginator': paginator,
            'suggestion': None,
        }

        if self.results and hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())
        return render_to_response(self.template, context, context_instance=self.context_class(self.request))



