from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import hashlib
from django.conf import settings
from payu.utils import generate_hash
from django.http import HttpResponseRedirect, HttpResponse
import uuid
from django.contrib.auth.models import User


def my_random_string(string_length=10):
	"""Returns a random string of length string_length."""
	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length]

def buy_order(request):
	user=Userprofile.objects.get(user_id=request.user.id)
	mobile=user.mobile
	initial = 'mr'
	fname=request.user.username
	lname=request.user.username
	pnumber=mobile
	email=request.user.email
	txnid=my_random_string(8)
	cleaned_data = {'key': settings.PAYU_INFO['merchant_key'],
					'txnid':txnid,'amount': request.COOKIES.get('price'),
					'productinfo':request.COOKIES.get('banner'),
					'firstname':fname,
					'email': email,
					'udf1':'', 'udf2': '', 'udf3': '',
					'udf4': '', 'udf5': '', 'udf6': '',
					'udf7': '','udf8': '', 'udf9': '', 'udf10': ''}
	hash_o = generate_hash(cleaned_data)
	print'id', txnid
	response= HttpResponse('''\
		<html>
			<head><title>Redirecting...</title></head>
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
			<script language='javascript'>window.onload = function(){ document.forms['payu'].submit() }</script>
			</html>'''% (settings.PAYU_INFO['payment_url'],
						 fname,                      
						 settings.PAYU_INFO['surl'],
						 pnumber,
						 settings.PAYU_INFO['merchant_key'],
						 hash_o,
						 settings.PAYU_INFO['curl'],
						 settings.PAYU_INFO['furl'],
						 txnid,
						 request.COOKIES.get('banner'),
						 request.COOKIES.get('price'),
						 email,
						 ))
	response.set_cookie('initial',initial)
	response.set_cookie('fname',fname)
	response.set_cookie('lname',lname)
	response.set_cookie('pnumber',pnumber)
	response.set_cookie('email',email)
	return response

def paid_user(request):
	initial = 'mr'
	fname=request.POST.get('fname',request.COOKIES.get('name'))
	lname=request.POST.get('lname',request.COOKIES.get('name'))
	pnumber=request.POST.get('pnumber',request.COOKIES.get('mobile'))
	email=request.POST.get('email',request.COOKIES.get('email'))
	txnid=my_random_string(8)
	cleaned_data = {'key': settings.PAYU_INFO['merchant_key'],
					'txnid':txnid,'amount': request.COOKIES.get('plan'),
					'productinfo':request.COOKIES.get('plan'),
					'firstname':fname,
					'email': email,
					'udf1':'', 'udf2': '', 'udf3': '',
					'udf4': '', 'udf5': '', 'udf6': '',
					'udf7': '','udf8': '', 'udf9': '', 'udf10': ''}
	hash_o = generate_hash(cleaned_data)
	response= HttpResponse('''\
		<html>
			<head><title>Redirecting...</title></head>
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
			<script language='javascript'>window.onload = function(){ document.forms['payu'].submit() }</script>
			</html>'''% (settings.PAYU_INFO['payment_url'],
						 fname,
						 settings.PAYU_INFO['surl1'],
						 pnumber,
						 settings.PAYU_INFO['merchant_key'],
						 hash_o,
						 settings.PAYU_INFO['curl'],
						 settings.PAYU_INFO['furl'],
						 txnid,
						 request.COOKIES.get('plan'),
						 request.COOKIES.get('plan'),
						 email,
						  ))
	return response
