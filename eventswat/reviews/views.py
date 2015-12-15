from django.core.exceptions import ObjectDoesNotExist
from django import http
from django.db import models
from reviews.forms import ReviewForm
import urllib
from reviews.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt


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
    if request.is_ajax():
        if request.method == 'POST':
            print "enter"
            review=Review()
            review.name=request.POST.get('name')
            print review.name
            review.email=request.POST.get('email')
            print review.email
            review.rating=request.POST.get('rating')
            print review.rating
            review.content=request.POST.get('content')
            print review.content
            review.event_id=request.POST.get('postevent')
            print review.event_id
            review.save()
            msg = "The operation has been received correctly."
    else:
        msg = "Fail"

    return HttpResponse(msg)
    




    # if request.method == 'POST':
    #     # Fill out some initial data fields from an authenticated user, if present
    #     data = request.POST.copy()
   
    #     # Look up the object we're trying to review about
    #     ctype = data.get("content_type")
    #     object_pk = data.get("object_pk")
    #     if ctype is None or object_pk is None:
    #         return ReviewPostBadRequest("Missing content_type or object_pk field.")
    #     try:
    #         model = models.get_model(*ctype.split(".", 1))
    #         target = model._default_manager.get(pk=object_pk)
    #     except TypeError:
    #         return ReviewPostBadRequest(
    #             "Invalid content_type value: %r" % escape(ctype))
    #     except AttributeError:
    #         return ReviewPostBadRequest(
    #             "The given content-type %r does not resolve to a valid model." % \
    #                 escape(ctype))
    #     except ObjectDoesNotExist:
    #         return ReviewPostBadRequest(
    #             "No object matching content-type %r and object PK %r exists." % \
    #                 (escape(ctype), escape(object_pk)))
   
    #     # Construct the review form
    #     form = ReviewForm(target, data=data)
   
    #     # If there are errors or if we requested a preview show the review
    #     if form.errors:
    #         template_list = [
    #             "reviews/%s_%s_preview.html" % tuple(str(model._meta).split(".")),
    #             "reviews/%s_preview.html" % model._meta.app_label,
    #             "reviews/preview.html",
    #         ]
    #         return render_to_response(
    #             template_list, {
    #                 "review" : form.data.get("review", ""),
    #                 "form" : form,
    #             },
    #             RequestContext(request, {})
    #         )
   
    #     # Otherwise create the review
    #     review = form.get_review_object()
    #     if request.user.is_authenticated():
    #         review.user = request.user
   
    #     # Save the review
    #     review.save()
    #     return HttpResponseRedirect(data.get('next'))
    #     add_form = ReviewForm(target, data=data)
    # # else:
    # #     add_form = ReviewForm(target, data=data)

    # return render_to_response("about-us.html", context_instance=RequestContext(request))

