from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('employers.views.misc',
	   url(r'^$', RedirectView.as_view(url=reverse_lazy('employers_dashboard'))),
	   url(r'^dashboard/$', 'dashboard', name='employers_dashboard'),
)


urlpatterns += patterns('employers.views.timeentries',
	   url(r'^timeentries/$', 'list', name='employers_timeentries_list'),
        url(r'^timeentries/(?P<identifier>\d+)/?$', 'detail', name='employers_timeentries_detail'), 
        url(r'^timeentries/approve/(?P<identifier>\d+)/?$', 'approve', name='employers_timeentries_approve'), 
        url(r'^timeentries/update/(?P<identifier>\d+)/?$', 'update', name='employers_timeentries_update'), 
)

urlpatterns += patterns('employers.views.transactions',
        url(r'^incompletetransactions/$', 'list', name='employers_incompletetransactions_list'),
        url(r'^transactions/(?P<identifier>\d+)/?$', 'detail', name='employers_transactions_detail'),                        
)

urlpatterns += patterns('employers.views.orders',
        url(r'^orders/$', 'list', name='employers_orders_list'),
        url(r'^orders/(?P<identifier>\d+)/?$', 'detail', name='employers_orders_detail'),
        url(r'^orders/update/(?P<identifier>\d+)/?$', 'update', name='employers_orders_update'),
        url(r'^orders/create$', 'create', name='employers_orders_create'),
        url(r'^orders/delete/(?P<identifier>\d+)/?$', 'delete', name='employers_orders_delete'),
)

urlpatterns += patterns('employers.views.assignments',
        url(r'^orders/(?P<orderid>\d+)/unassign/(?P<assignmentid>\d+)/?$', 'unassign', name='employers_assignments_unassign'),
        url(r'^orders/(?P<orderid>\d+)/update/(?P<assignmentid>\d+)/?$', 'update', name='employers_assignments_update'),
)