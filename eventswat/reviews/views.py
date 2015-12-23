from reviews.models import *
from reviews.forms import *
from itertools import ifilter
from django.shortcuts import render
from django.template import Context
from django.template.response import TemplateResponse
from django.template import RequestContext
from postevent.models import Postevent
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse

@csrf_exempt
def feedback(request):
	if request.is_ajax():
		if request.method == 'POST':
			print "enter"
			form = WebsiteFeedbackForm(request.POST)
			if form.is_valid():
				print "form is valid"
				# print "form",form
				form.save()
				print "save"
			else:
				form = WebsiteFeedbackForm()

			msg = "The operation has been received correctly."
	else:
		msg = "Fail"

	return HttpResponse(msg)

@csrf_exempt
def comment(request):
	comment_form = CommentForm(request.POST or None)
	postevent = Postevent.objects.all()
	if request.is_ajax():
		if request.method == "POST":
			if request.user.is_authenticated():
				if comment_form.is_valid():
					print "comment"
					temp = comment_form.save(commit=False)
					temp.postevent_id = request.POST.get('postent')
					temp.content = request.POST.get('content',request.COOKIES.get('content'))
					print temp.content,"content"
					temp.rating = request.POST.get('rating',request.COOKIES.get('rating'))
					print temp.rating,"rating"
					parent = comment_form['parent'].value()
					if parent == "":
						temp.path = []
						temp.save()
						id = temp.id
						print "id",id
						temp.path = [id]
					else:

						node = Comment.objects.get(id = parent)
						temp.depth = node.depth + 1
						s = str(node.path)
						temp.path = eval(s)
						temp.save()
						id= temp.id
						temp.path.append(id)

					temp.save()
		msg = "The operation has been received correctly."
	else:
		msg = "Fail"

	return HttpResponse(msg)
	