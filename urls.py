from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler500 = 'djangotoolbox.errorviews.server_error'
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'siteapp.views.page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>(?!admin)[a-zA-Z0-9\_\-]+)$', 'siteapp.views.page'),
)

urlpatterns += staticfiles_urlpatterns()
