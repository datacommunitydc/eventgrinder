import sys
import os, os.path
from logging import error


sys.path= [os.path.join(os.path.dirname(__file__), 'shared'), os.path.join(os.path.dirname(__file__), '.')]+sys.path






def namespace_manager_default_namespace_for_request():
    import os
    if os.environ.get('PATH_INFO', '').startswith('/_ah') and not os.environ.get('PATH_INFO', '').startswith('/_ah/login_required') or os.environ.get('PATH_INFO', '').startswith('/_ah/upload'): return ''
    if os.environ.get('HTTP_HOST'):
        return os.environ.get('HTTP_HOST').split(':')[0]
    else:
        return ''
        
remoteapi_CUSTOM_ENVIRONMENT_AUTHENTICATION = (
    'HTTP_X_APPENGINE_INBOUND_APPID', ['techevents'])