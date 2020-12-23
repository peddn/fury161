from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
if os.getenv('HOST_1') is not None:
    if os.getenv('HOST_2') is None:
        ALLOWED_HOSTS = [os.getenv('HOST_1'), 'localhost']
    else:
        ALLOWED_HOSTS = [os.getenv('HOST_1'), os.getenv('HOST_2'), 'localhost']
else:
    ALLOWED_HOSTS = ['localhost']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',                                             # the postgresql database name
        'USER': '',                                             # the postgresql user name
        'PASSWORD': '',                                         # the postgresql user password
        'HOST': 'localhost',
        'PORT': ''                                              # leave this blank
    }
}

try:
    from .local import *
except ImportError:
    pass
