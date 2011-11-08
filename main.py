import sys, os
from google.appengine.ext.webapp import util


sys.path= [os.path.join(os.path.dirname(__file__), 'shared'), os.path.join(os.path.dirname(__file__), '.')]+sys.path


# Django imports and other code go here...
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers, django.core.handlers.wsgi

from django.conf import settings
settings.ROOT_URLCONF="urls"




application = django.core.handlers.wsgi.WSGIHandler()
