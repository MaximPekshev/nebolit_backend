# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0872810/data/www/backend.annasoft.site/nebolit')
sys.path.insert(1, '/var/www/u0872810/data/nebolit_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'nebolit.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()