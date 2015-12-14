# from core import helper
from eventswat import globals
from django.conf import settings
from django.utils import translation
from eventswat.util import get_client_ip
from eventswat.util import *
from events.models import *


#Middleware class for finding global_lanugage, global_country, global_ip when user enter into the website
class Global(object):
    global_country=''
    global_ip=''
    global_city=''
    global_city_id=''
    
    # def process_request(self, request):
    #     globals.request = request
    #     globals.user = getattr(request, 'user', None)
    #     globals.ip = get_client_ip(request)
    #     if ',' in globals.ip:
    #         globals.ip = globals.ip.split(',')[0].strip()
    #     globals.sess = request.session.session_key
    #     self.global_country=get_global_country(request)
    #     self.global_city=get_global_city(request)
    #     self.global_city_id=get_global_city_id(request)
    #     self.global_ip= globals.ip
    
    def process_response(self, request, response):
        """while response set cookie for language"""
        if self.global_country:
            country=self.global_country
            response.set_cookie("country", 
                country, max_age = 365 * 24 * 60 * 60)
        if self.global_ip:
            ip=self.global_ip
            response.set_cookie("ip", 
                ip, max_age = 365 * 24 * 60 * 60)
        if self.global_city:
            city=self.global_city
            response.set_cookie("city", 
                city, max_age = 365 * 24 * 60 * 60)
        if self.global_city_id:
            city=self.global_city_id
            response.set_cookie("global_city_id", 
                city, max_age = 365 * 24 * 60 * 60)
        return response

class User(Global):
    def __init__(self, *args, **kwargs):
        import warnings
        warnings.warn(
            DeprecationWarning,
            stacklevel=2
        )
        super(User, self).__init__(*args, **kwargs)
