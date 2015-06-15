from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^', include('Ngo.news.urls')),

                       url(r'^user/', include('Ngo.persons.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'},
                           name='login'),

                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': 'home'},
                           name='logout'),

                       )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
