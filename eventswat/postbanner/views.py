from payu.views import payu_transaction
from postbanner.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from postbanner.models import PostBanner


class JSONResponse(HttpResponse):

	def __init__(self, data):
		super(JSONResponse, self).__init__(
			simplejson.dumps(data), mimetype='application/json')

@csrf_exempt
@login_required(login_url='/?lst=2')
def banner(request):
    if request.user.is_authenticated():
        try:
            temporary_banner = TempBanner.objects.get(temp_user_id=request.user.id)
            temporary_banner.delete()
        except TempBanner.DoesNotExist:
            pass
        if request.method == 'POST' and request.POST['status'] == 'failure':
            message = 'Unable to complete your transaction'
        else:
            message = ''
        banner_list = BannerPlan.objects.all()
        banner_plans = list(set(banner_list))
        posted_banner = PostBanner.objects.filter(admin_status='true')
        return render_to_response("uploadbanner.html",
                                  {'banner_plans': banner_plans,
                                  'posted_banner':posted_banner,
                                  'message':message},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')    

@csrf_exempt
@login_required(login_url='/?lst=2')
def upload_banner(request):
    if request.method == 'POST':
        tempbanner = TempBanner()
        tempbanner.temp_user_id = request.user.id
        tempbanner.temp_bannerplan = BannerPlan.objects.get(
            id=request.POST.get('hidden_bannerplan'))
        tempbanner.temp_banner = request.FILES.get('banner')
        tempbanner.temp_link = request.POST['link']
        tempbanner.save()
        firstname = request.user.username
        email = request.user.email
        mobile = Userprofile.objects.values('mobile').get(email=email)['mobile']
        productinfo = tempbanner.temp_bannerplan.id
        amount = request.POST.get('banner_price')
        response  = HttpResponse(payu_transaction(firstname, email,
                             mobile, productinfo, amount))
        return response
    else:
        return HttpResponseRedirect("/banner/")
