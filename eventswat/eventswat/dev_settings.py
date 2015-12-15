"""
Django settings for events project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

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
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    'eventswat',
    'haystack',
    'search',
    'payu', 
    'commerce',   
    'postbanner',
    # 'social.apps.django_app.default',
    # 'tracking',
    'reviews',
    'worker',
    'south',
    'postevent',
    'usermanagement',
    'logs',
)

SITE_ID = 1

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
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'events.middleware.Global',

)

ROOT_URLCONF = 'events.urls'

WSGI_APPLICATION = 'events.wsgi.application'


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

MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'events.context_processors.eventtype',
    "django.contrib.messages.context_processors.messages",
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'

GEOIP_PATH = os.path.join(os.path.dirname(__file__), 'static/geoip/')
# GEOIP_PATH = os.path.join(os.path.dirname(__file__), '../static/geoip/')

#img upload by pradeepa
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

PAYU_INFO = {
             'merchant_key': "gtKFFx",
             'merchant_salt': "eCwWELxi",
             # for production environment use 'https://secure.payu.in/_payment'
             'payment_url': 'https://test.payu.in/_payment',
             #success url for hotel
             'surl':'http://localhost:8000/upload_banner',
             'surl1':'http://localhost:8000/success',
             'curl':'http://localhost:8000/post_event_v2',
             'furl':'http://localhost:8000/post_event_v2',
            }
