from payu.utils import generate_hash
from payu.models import PayuDetails

import uuid
import hashlib
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from postbanner.models import PostBanner,TempBanner
from commerce.models import Order, Transaction
from templated_email import send_templated_mail


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def payu_transaction(fname, email, mobile, product, amount):
    """
    This function redirect to payu page when user given following fields.
    1.Firstname
    2.Email
    3.Mobile
    4.Product details
    5.Amount
    """
    current_site = Site.objects.get_current()
    success = current_site.domain + '/' + settings.PAYU_INFO['surl']
    cancel = current_site.domain + '/' + settings.PAYU_INFO['curl']
    failure = current_site.domain + '/' + settings.PAYU_INFO['furl']
    txnid = my_random_string(8)
    cleaned_data = {'key': settings.PAYU_INFO['merchant_key'],
                    'txnid': txnid, 'amount': amount, 'productinfo': product,
                    'firstname': fname, 'email': email, 'udf1': '', 'udf2': '',
                    'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '', 'udf7': '',
                    'udf8': '', 'udf9': '', 'udf10': ''}
    hash_o = generate_hash(cleaned_data)
    response = HttpResponse('''\
        <html><head><title>Redirecting...</title></head>
            <body>
                <form action='%s' method='post' name="payu">
                    <input type="hidden" name="firstname" value="%s" />
                    <input type="hidden" name="surl" value="%s" />
                    <input type="hidden" name="phone" value="%s" />
                    <input type="hidden" name="key" value="%s" />
                    <input type="hidden" name="hash" value ="%s" />
                    <input type="hidden" name="curl" value="%s" />
                    <input type="hidden" name="furl" value="%s" />
                    <input type="hidden" name="txnid" value="%s" />
                    <input type="hidden" name="productinfo" value="%s" />
                    <input type="hidden" name="amount" value="%s" />
                    <input type="hidden" name="email" value="%s" />
                    <input type="hidden" value="submit">
                </form>
            </body>
            <script language='javascript'>
                window.onload = function(){
                    document.forms['payu'].submit() }
            </script>
        </html>''' % (settings.PAYU_INFO['payment_url'], fname, success,
                      mobile, settings.PAYU_INFO['merchant_key'], hash_o,
                      cancel, failure, txnid, product, amount, email, ))
    return response


@csrf_exempt
def payu_data(request):
    """" Store the payu responsed data when payment successs"""
    if request.method == 'POST':
        payu = PayuDetails()
        payu.mihpayid = request.POST.get('mihpayid')
        payu.mode = request.POST.get('mode')
        payu.status = request.POST.get('status')
        payu.txnid = request.POST.get('txnid')
        payu.key = request.POST.get('key')
        payu.amount = request.POST.get('amount')
        payu.discount = request.POST.get('discount')
        payu.productinfo = request.POST.get('productinfo')
        payu.hash_key = request.POST.get('hash')
        payu.error_Message = request.POST.get('error_Message')
        payu.bank_code = request.POST.get('bankcode')
        payu.pg_type = request.POST.get('PG_TYPE')
        payu.band_ref_number = request.POST.get('bank_ref_num')
        payu.save()
        if request.POST['status'] == 'success':
            print 'success'
            uploadbanner = PostBanner()
            temporary_banner = TempBanner.objects.get(temp_user_id=request.user.id)
            print 'temporary_banner', temporary_banner.temp_user_id
            uploadbanner.bannerplan_id = request.POST.get('productinfo')
            banner = TempBanner.objects.values('temp_banner').get(temp_user_id=temporary_banner.temp_user_id)['temp_banner']
            print 'banner', banner
            uploadbanner.banner = banner
            uploadbanner.link=temporary_banner.temp_link
            uploadbanner.user_id=temporary_banner.temp_user_id
            uploadbanner.save()
            temporary_banner.delete()
            send_templated_mail(
              template_name = 'banner',
              subject = 'Uplaod Banner',
              from_email = 'eventswat@gmail.com',
              recipient_list = [request.user.email ],
              context={
                       'user': request.user,

              },
            )
            order = Order()
            order.banner = uploadbanner
            order.banner_plan_id = request.POST.get('productinfo')
            order.save()
            trans = Transaction()
            trans.user = request.user
            trans.transaction_mode = 'online'
            trans.post_type = 'banner'
            trans.order_id = order.id
            trans.payu = payu
            trans.save()
    return HttpResponseRedirect("/banner/")
