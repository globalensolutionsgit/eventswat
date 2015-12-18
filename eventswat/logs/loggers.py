import logging
import datetime
from eventswat import globals, user_ip
from templated_email import send_templated_mail
from django.core.mail import send_mail
from django.conf import settings

class MyDbLogHandler(logging.Handler): # Inherit from logging.Handler
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        try:
            from logs.models import ErrorLog
            logEntry =ErrorLog()
            logEntry.level = record.levelname 
            logEntry.error_msg = record.getMessage(), record.exc_info      
            # logEntry.ip_address = user_ip()
            # print "logEntry.ip_address", logEntry.ip_address
            logEntry.page = record.args, record.lineno, record.pathname 
            logEntry.datetime = datetime.datetime.now()
            logEntry.user = record.request.user
            logEntry.admin_status = 'open'
            logEntry.save()
        except:            
            pass
        
        if record.levelname == 'ERROR':
           send_templated_mail(
                template_name='error',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['kalai@globalensolutions.com'],
                context={
                         'errorlevel': record.levelname,
                         'error_msg': [record.getMessage(), record.exc_info],
                         # 'error_ip': globals.ip,
                         'error_user': record.request.user,
                         'error_line' : [record.lineno, record.pathname],
                },
            )   