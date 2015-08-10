from django.conf.urls import patterns, url


urlpatterns = patterns('Ngo.persons.views',
                       url(r'^$', 'user_home', name='user-home'),
                       url(r'^addadmin/$', 'add_admin'),
                       url(r'^addexpert/$', 'add_expert'),
                       url(r'^addngo/$', 'add_NGO'),
                       url(r'^add_pic/$', 'add_pic'),
                       url(r'^delete/(\w{1,100})/', 'delete_NGO'),
                       url(r'^user/delete/(\w{1,100})/', 'delete_user'),
                       url(r'^changepass/$', 'change_password'),
)