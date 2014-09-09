from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import hello
from views import current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
)
