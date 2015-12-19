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
    'django.contrib.sites',
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
    'social_auth',

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
    'django.contrib.sessions.middleware.SessionMiddleware',
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

COMPRESS_ENABLED = True

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
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
             'surl':'postbanner/payment_success/',
             'curl':'post_event',
             'furl':'post_event',
            }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eventswat@gmail.com'
EMAIL_HOST_PASSWORD = 'street11'
EMAIL_PORT = 587

LATEST_INDEX=1
TRACK_PAGEVIEWS = True


TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)
LATEST_INDEX=1


# code by priya for login using socail_auth

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'events.context_processors.globalactivity',
    "django.contrib.messages.context_processors.messages",
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

AUTH_USER_EMAIL_UNIQUE = True

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID='756365291174460'
FACEBOOK_API_SECRET='aa6ec915216469c245452be12eb4371c'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'pl_PL',
  'fields': 'id, name, email',
}


SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/login-error/'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SOCIAL_AUTH_PIPELINE = (
'social_auth.backends.pipeline.social.social_auth_user',
'social_auth.backends.pipeline.associate.associate_by_email',
'social_auth.backends.pipeline.user.get_username',
'social_auth.backends.pipeline.user.create_user',
'social_auth.backends.pipeline.social.associate_user',
'social_auth.backends.pipeline.user.update_user_details',

)

SOCIAL_AUTH_ENABLED_BACKENDS = 'google'
GOOGLE_OAUTH2_CLIENT_ID='68245467057-u35gr8trm5ofqq5b60dh2eea9a7uosdc.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET ='haUGRT9sLvZJmcZALyk1tVUX'
GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_USER_MODEL = 'auth.User'
GOOGLE_OAUTH2_USE_DEPRECATED_API = True

SITE_ID = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        },
    'handlers': {
        'file':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'eventswatlog.log',
            'formatter': 'verbose'
        },
        'db':{
            'level': 'WARNING',
            'class': 'logs.loggers.MyDbLogHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['db', 'file'],
            'level': 'WARNING',
            'propagate': False,
            },
        'myapplog': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
            }
        }
}

DEFAULT_FROM_EMAIL = 'eventswat@gmail.com'

