from payu.views import payu_transaction
from django.http import HttpResponseRedirect, HttpResponse

def payment(request):
    """postbanner payu payment process"""
    # These are mandatory fields for payment process.You can reuse anywhere #
    firstname = 'muthu'
    email = 'spmuthu21@gmail.com'
    mobile = '7845738923'
    productinfo = 'dsfgdghsdfggdsfg'
    amount = '10000'
    return HttpResponse(payu_transaction(firstname,email,mobile,productinfo,amount))
