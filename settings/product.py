from base import *

DEBUG = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#devserver
MIDDLEWARE_CLASSES += ()   # Add extra classes here
INSTALLED_APPS += ()       # Add extra apps here

try:
    from local import *
except:
    pass

