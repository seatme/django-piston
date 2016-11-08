from __future__ import absolute_import
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'api/', include('test_project.apps.testapp.urls'))
)
