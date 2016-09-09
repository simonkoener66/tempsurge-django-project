from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
                       # (r'^new/$', 'new'),
                       # (r'^check-availability', 'check_username_availability'),
                       # (r'^activation/(?P<id>\d+)/(?P<key>[-\w]+)/$', 'activation'),
                       (r'^profile/$', 'profile'),
                       (r'^settings/$', 'settings'),
                       # (r'^change-email/(?P<id>\d+)/(?P<key>[-\w]+)/$', 'change_email'),
                       # (r'^password/$', 'password'),
                       (r'^cities-of-country', 'cities_of_country'),
                       url(r'^login/$', 'sign_in', name='sign_in'),
                       (r'^logout/$', 'sign_out'),
                       (r'^recover/$', 'recover'),
                       (r'^reset/(?P<id>\d+)/(?P<key>[-\w]+)/$', 'reset'),
)