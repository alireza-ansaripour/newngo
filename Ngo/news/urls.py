from django.conf.urls import patterns, url

urlpatterns = patterns('Ngo.news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'create_article'),
                       url(r'^edit/$', 'edit'),
                       url(r'^article/(\w{1,30})/$', 'show_article'),
                       url(r'^article/(\w{1,30})/(\w{1,2})/$', 'update_news'),
                       url(r'^delete/(\d{1,7})/d/$', 'delete_news'),
                       url(r'^shownews/$', 'show_new_news'),
                       url(r'editnews/$', 'show_news'),
                       url(r'^accounts/profile/$', 'user_home'),
                       url(r'^news/(\w{1,2})/$', 'filter_news'),
                       url(r'^ngo/(\w{1,10})/$', 'show_NGO'),
                       url(r'^ngo/(\w{1,10})/(\w{1,10})/$', 'request_ngo')
)