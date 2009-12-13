from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^$', 'taskhood.tasks.views.index'), #points to the views.py file and index function within
    (r'^main/', 'taskhood.tasks.views.main'), 
)
