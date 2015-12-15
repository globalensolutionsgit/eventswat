"""
Django settings for events project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import smtplib
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# for img upload
FOR_IMG=os.path.join(os.path.dirname(__file__), 'static/img/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fvvtbnjey!qj-r1e!+1b+imz73bn!zsvz_r51^87jlz^w250*6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'events',
    'eventswat',
    'haystack',
    'search',
    'payu',
    'commerce',
    'postbanner',
    'reviews',
    'worker',
    'south',
    'postevent',
    'usermanagement',
    'logs',
    'core',
    'tracking',


)




HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventswat.urls'

WSGI_APPLICATION = 'eventswat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'evewat',                        # Or path to database file if using sqlite3.
        'USER': 'root',                          # Not used with sqlite3.
        'PASSWORD': 'root',                      # Not used with sqlite3.
        'HOST': 'localhost',                     # Set to empty string for localhost. Not used with sqlite3.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)
TEMPLATE_DIRS = os.path.join((os.path.dirname(__file__)), 'templates')

MEDIA_ROOT = os.path.join((os.path.dirname(__file__)), 'media')
print 'MEDIA_ROOT', MEDIA_ROOT

MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'events.context_processors.globalactivity',
    "django.contrib.messages.context_processors.messages",
    # 'social_auth.context_processors.social_auth_by_name_backends',
    # 'social_auth.context_processors.social_auth_backends',
    # 'social_auth.context_processors.social_auth_by_type_backends',
    # 'social_auth.context_processors.social_auth_login_redirect',
)

AUTH_USER_EMAIL_UNIQUE = True

# from django.contrib.auth.models import User
# User._meta.get_field("username")._unique = False


LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY ='1659129517705839'
SOCIAL_AUTH_FACEBOOK_SECRET ='8b2ebde6051b128b0f453b8384bc5989'
URL_PATH = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='1080122031533-a8hiac9frtar20hc6clpduj53498o4hn.apps.googleusercontent.com '
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='AAUhtKjmWVDYSsBmAGmDDzwO'

COMPRESS_ENABLED = True

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
FLEXSELECT = {
    'include_jquery': True,
}
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'

# GEOIP_PATH = os.path.join(os.path.dirname(__file__), 'static/geoip/')
# GEOIP_PATH = os.path.join(os.path.dirname(__file__), '../static/geoip/')

#img upload by pradeepa
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

PAYU_INFO = {
             'merchant_key': "gtKFFx",
             'merchant_salt': "eCwWELxi",
             # for production environment use 'https://secure.payu.in/_payment'
             'payment_url': 'https://test.payu.in/_payment',
             #success url for hotel
             'surl':'http://www.eventswat.com/upload_banner',
             'surl1':'http://www.eventswat.com/success',
             'curl':'http://www.eventswat.com/post_event',
             'furl':'http://www.eventswat.com/post_event',
            }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eventswat@gmail.com'
EMAIL_HOST_PASSWORD = 'street11'
EMAIL_PORT = 587



TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

# You can use a shortcut version
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

# You can also use a class directly
from templated_email.backends.vanilla_django import TemplateBackend
TEMPLATED_EMAIL_BACKEND = TemplateBackend

LATEST_INDEX=1

