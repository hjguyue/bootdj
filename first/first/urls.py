from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import hello
from views import current_datetime
from views import display_meta
from views import showDB
from books.views import search
from contact.views import contact
from contact.views import thanks

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url('^display/$', display_meta),
    url('^showDB/$', showDB),
    url('^search/$', search),
    url('^contact/$', contact),
    url('^contact/thanks/$', thanks),
)
