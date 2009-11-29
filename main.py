# main.py
 
import os, sys
os.environ["DJANGO_SETTINGS_MODULE"] = "taskhood.settings"
sys.path.append("/home/brox/tmp/mashname")
 
# Google App Engine imports.
from google.appengine.ext.webapp import util

# Django version
from google.appengine.dist import use_library
use_library('django', '1.1')
 
# Force Django to reload its settings.
from django.conf import settings
settings._target = None
 
import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

def log_exception(*args, **kwds):
   logging.exception('Exception in request:')
 
# Log errors. 
django.dispatch.Signal.connect(    
   django.core.signals.got_request_exception, 
   log_exception)  

# Unregister the rollback event handler. 
django.dispatch.Signal.disconnect(     
   django.core.signals.got_request_exception,     
   django.db._rollback_on_exception)
 
def main():
	# Create a Django application for WSGI.
	application = django.core.handlers.wsgi.WSGIHandler()
 
	# Run the WSGI CGI handler with that application.
	util.run_wsgi_app(application)
 
if __name__ == "__main__":
	main()

