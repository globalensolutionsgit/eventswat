import threading
globals = threading.local()

#For finding user global ip, that is internet ip address
def user_ip():
  if hasattr(globals, 'ip'):
    return globals.ip
  else:
    return None

# from django.conf import settings
# from django.contrib.auth import models as auth_models
# from django.contrib.auth.management import create_superuser
# from django.db.models import signals

# from core.db import import_defaults

# # From http://stackoverflow.com/questions/1466827/ --
# #
# # Prevent interactive question about wanting a superuser created.  (This code
# # has to go in this otherwise empty "models" module so that it gets processed by
# # the "syncdb" command during database creation.)
# signals.post_syncdb.disconnect(
#     create_superuser,
#     sender=auth_models,
#     dispatch_uid='django.contrib.auth.management.create_superuser')


# # Create our own test user automatically.

# def create_testuser(app, created_models, verbosity, **kwargs):
#   if not settings.DEBUG:
#     return
#   try:
#     auth_models.User.objects.get(username='root')
#   except auth_models.User.DoesNotExist:
#     print '*' * 80
#     print 'Creating test user -- login: test, password: test'
#     print '*' * 80
#     assert auth_models.User.objects.create_superuser('root', 'root@gmail.com', 'root')
#   else:
#     print 'Test user already exists.'

# signals.post_syncdb.connect(create_testuser,
#     sender=auth_models, dispatch_uid='common.models.create_testuser')
    
    
    
# signals.post_syncdb.connect(import_defaults, sender=auth_models)

# from django.contrib.auth.forms import AuthenticationForm

# AuthenticationForm.base_fields['username'].max_length = 150
# AuthenticationForm.base_fields['username'].widget.attrs['maxlength'] = 150
# AuthenticationForm.base_fields['username'].validators[0].limit_value = 150


# import haystack
