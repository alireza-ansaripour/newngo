from django.conf.urls import patterns, url


urlpatterns = patterns('Ngo.persons.views',
                       url(r'^$', 'user_home', name='user-home'),
                       url(r'^addadmin/$', 'add_admin'),
                       url(r'^addexpert/$', 'add_expert'),
                       url(r'^addngo/$', 'add_NGO'),
                       url(r'^add_pic/$', 'add_pic'),
)