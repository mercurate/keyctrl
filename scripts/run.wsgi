import os
import site

PROJECT_ROOT = os.path.dirname(__file__)
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, '../'))

ALLDIRS = [os.path.join(ROOT_PATH, 'ENV/lib/python2.7/site-packages'), os.path.join(ROOT_PATH, 'sites')]

prev_sys_path = list(sys.path) 
for directory in ALLDIRS:
    site.addsitedir(directory)

new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

