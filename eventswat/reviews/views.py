from django.core.exceptions import ObjectDoesNotExist
from django import http
from django.db import models
from reviews.forms import *
import urllib
from reviews.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from itertools import ifilter


# class ReviewPostBadRequest(http.HttpResponseBadRequest):
#     """
#     Response returned when a review post is invalid. If ``DEBUG`` is on a
#     nice-ish error message will be displayed (for debugging purposes), but in
#     production mode a simple opaque 400 page will be displayed.
#     """
#     def __init__(self, why):
#         super(ReviewPostBadRequest, self).__init__()
#         if settings.DEBUG:
#             self.content = render_to_string("reviews/400-debug.html", {"why": why})

@csrf_exempt  
def post(request):
    form = WebsiteFeedbackForm(request.POST)
    if request.is_ajax():
        if request.method == 'POST':
            print "enter"
            
            if form.is_valid():
                  return HttpResponseRedirect('/thanks/')
            else:
                form = WebsiteFeedbackForm()
            
            msg = "The operation has been received correctly."
    else:
        msg = "Fail"

    return HttpResponse(msg)
    


# def home(request):
#     print "enter"
#     postevent = Postevent.objects.all()
#     context = base_context(request)
   
#     form = CommentForm(request.POST or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             temp = form.save(commit=False)
#             parent = form['parent'].value()
            
#             if parent == '':
#                 #Set a blank path then save it to get an ID
#                 temp.path = []
#                 temp.save()
#                 id = int(temp.id) 
#                 temp.path = [id] 
#             else:
#                 #Get the parent node
#                 node = Comment.objects.get(id=parent)
#                 temp.depth = node.depth + 1
#                 s = str(node.path)
#                 temp.path = eval(s)

                
#                 #Store parents path then apply comment ID
#                 temp.save()
#                 id= int(temp.id) 
#                 temp.path.append(id) 
                
                
#             #Final save for parents and children
#             temp.postevent = Postevent.objects.get(pk=form.cleaned_data['postevent_id'])
#             print temp.postevent,"temp.postevent"
#             temp.save()
            
    
#     #Retrieve all comments and sort them by path
#     comment_tree = Comment.objects.all().order_by('path')
#     context['postevent'] = postevent 
#     context['form'] = form           
#     return render(request, 'index_comments.html',context)
#     # return render_to_response("index_comments.html",{'events':postevent}, context_instance=RequestContext(request))
