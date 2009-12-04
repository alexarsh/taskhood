from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^$', 'taskhood.tasks.views.index'),

)
