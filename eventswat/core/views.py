# from django.shortcuts import render_to_response, get_object_or_404
# from django.template.context import RequestContext
# from django.views.decorators.csrf import csrf_protect
# from .models import Message
# from postevent.models import *

# # def home(request):
# #     context = {
# #         'messages': Message.objects.all(),
# #     }
# #     return render_to_response('core/home.html', context, context_instance=RequestContext(request))


# @csrf_protect
# def message(request):
# 	context = {
# 		'message': get_object_or_404(ThreadedComment),
# 		# 'messages': Message.objects.all(),
# 		# 'postevent': Postevent.objects.get(pk=id)
# 	}
	

# 	return render_to_response('core/message.html', context, context_instance=RequestContext(request))

# def comment_post(request):
# 	context = {
# 		'message': get_object_or_404(Message),
# 		'messages': Message.objects.all(),
# 		# 'postevent' : Postevent.objects.all(),
# 	}
	

# 	return render_to_response('core/message.html', context, context_instance=RequestContext(request))
