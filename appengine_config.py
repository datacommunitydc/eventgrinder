import sys
import os



sys.path= [os.path.join(os.path.dirname(__file__), 'shared'), os.path.join(os.path.dirname(__file__), '.')]+sys.path





def namespace_manager_default_namespace_for_request():
    import os
    if os.environ.get('HTTP_HOST'):
        return os.environ.get('HTTP_HOST').split(':')[0]
    else:
        return ''