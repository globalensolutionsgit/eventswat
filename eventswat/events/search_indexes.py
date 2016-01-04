import datetime
from haystack.indexes import *
from postevent.models import Postevent
from django.contrib.auth.models import User
from haystack.management.commands import update_index
from django.template import RequestContext

class PosteventIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    searchtext = CharField()
    eventcategory = IntegerField(model_attr='event_category__id')
    eventsubcategory = IntegerField(model_attr='event_subcategory__id')
    city = CharField(model_attr='city')
    country = CharField(model_attr='country', null=True)
    eventtitle = CharField(model_attr='event_title')
    payment=CharField(model_attr='payment')
    event_startdate_time=DateTimeField(model_attr='event_startdate_time')
    event_enddate_time=DateTimeField(model_attr='event_enddate_time')
    eventtype=CharField(model_attr='event_type', null=True)
    admin_status=IntegerField(model_attr='admin_status')
    keywords=MultiValueField(null=True)
    event_poster=MultiValueField(null=True)
    
    def autoUpdateRebuild_index(self):
        update_index.Command().handle()
        rebuild_index.Command().handle()

    def prepare_searchtext(self, obj):      
        text = []
        if obj.event_title:
            text.append(obj.event_title)
        # if obj.city:
        #     text.append(obj.city)

        text += self.keyword_search(obj)

        search = []
        for t in text:
            t = re.sub(r'[^\w]', ' ', t, flags=re.UNICODE).split(' ')
            for q in t:
                if q and (not re.match(r'[^\w]', q, flags=re.UNICODE)):
                    search.append(q)
        return ' '.join(search)

    def keyword_search(self, obj):        
        keywords = []
        event_keywords = {}
        for term in obj.keywords.all():
            keywords.append(term.keyword)
        return keywords    


    def get_model(self):
        return Postevent

    def index_queryset(self, **kwargs):
        postevent = Postevent.objects.all()
        return postevent
