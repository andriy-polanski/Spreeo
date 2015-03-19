from django.utils.translation import ugettext_lazy as _
"""
Django settings for dashboard_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iy4)%tt4(5&o-f1esote_6b0rq-s^2v8(j9k1!2b3i*@^lkl-#'

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
    'django.contrib.flatpages',
    'django.contrib.sites',
    'reflex',
    'dashboard',
    'south',
    'sorl.thumbnail',
    'bootstrap3_datetime'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dashboard_project.urls'

WSGI_APPLICATION = 'dashboard_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'reflexdashboard',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
        'ATOMIC_REQUESTS': True,
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

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

# Dashboard Navigation Menu

DASHBOARD_MAIN_NAVIGATION = [
    {
        'label': _('Dashboard Home'),
        'icon': 'fa-home',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Merchant Profile'),
        'icon': 'fa-gears',
        'url_name': 'dashboard:edit_profile',
    },
    {
        'label': _('Products'),
        'icon': 'fa-list',
        'url_name': 'dashboard:product_list',
    },
    {
        'label': _('Add new product'),
        'icon': 'fa-file-o',
        'url_name': 'dashboard:product_new',
    },
    {
        'label': _('Payment Gateway'),
        'icon': 'fa-money',
        'url_name': 'dashboard:edit_payment_gateway',
    },
    {
        'label': _('Store Categories'),
        'icon': 'fa-files-o',
        'url_name': 'dashboard:store_categories',
    },
    {
        'label': _('Shipping Options'),
        'icon': 'fa-truck',
        'url_name': 'dashboard:shipping_options',
    }   
]



#SORL Thumbnail

THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'reflex-dashboard'

MEDIA_ROOT = 'uploads/'
MEDIA_URL = '/uploads/'

