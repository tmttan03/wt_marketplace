from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kgd_mg)fl885(97$8+k*bc^84hxu#*^3ewj_84f&qepvrf+!x1'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tmttan03@gmail.com'
EMAIL_HOST_PASSWORD = 'hdilt2201400117'
EMAIL_PORT = 587

try:
    from .local import *
except ImportError:
    pass
