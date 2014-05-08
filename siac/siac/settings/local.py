# -*- encoding: utf-8 -*-
from .base import *
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.core.urlresolvers import reverse_lazy

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'siac_devel',
        'USER': 'siac',
        'PASSWORD': 'siac',
        'HOST': 'localhost',    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',      # Set to empty string for default.
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# Redireccina si el login fue incorrecto
LOGIN_URL = reverse_lazy('login')

# Variable que redirecciona cuando el login fue correcto
LOGIN_REDIRECT_URL = reverse_lazy('login')

# Variable que redirecciona cunado se hace logout
LOGOUT_URL = reverse_lazy('logout')


#parámetros para enviar correos
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hernanxavierp@gmail.com'
EMAIL_HOST_PASSWORD = 'X1v32rPR2012'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Variable para Guardian
ANONYMOUS_USER_ID = -1


###### Configuracion de la Aplicacion Django SUIT #######

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {

    'ADMIN_NAME': 'SIAC ADMINISTRACIÓN',
    'MENU_OPEN_FIRST_CHILD': True,
    'SHOW REQUIRED ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 50,

    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'sistema': 'icon-cog',
    },
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

##############################################