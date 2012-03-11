import sys, os
from google.appengine.ext.webapp import util




# Django imports and other code go here...
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers, django.core.handlers.wsgi

from django.conf import settings
settings.ROOT_URLCONF="urls"




application = django.core.handlers.wsgi.WSGIHandler()
