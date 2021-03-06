# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~

    Configuration settings.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
config = {}

# Configurations for the 'tipfy' module.




config['tipfy'] = {
    # Enable debugger. It will be loaded only in development.
    'middleware': [
        'tipfy.ext.debugger.DebuggerMiddleware',
    ],
    'apps_installed': [
        'apps.calendar',
        'apps.links',
    ],
}



config['tipfy.ext.session'] = {
    'secret_key': 'Ross M Karchner: OK Guy',
}

