from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('agencies.views.misc',
        url(r'^$', RedirectView.as_view(url=reverse_lazy('agencies_dashboard'))),
        url(r'^dashboard/$', 'dashboard', name='agencies_dashboard'),
)

urlpatterns += patterns('agencies.views.temps_views',
        url(r'^employees/$', 'listing', name='agencies_temps_listing'),
        url(r'^employees/(?P<identifier>\d+)/?$', 'show', name='agencies_temps_show'),
        url(r'^employees/create$', 'form', name='agencies_temps_add'),
        url(r'^employees/update/(?P<identifier>\d+)/?$', 'form', name='agencies_temps_edit'),
        url(r'^employees/delete/(?P<identifier>\d+)/?$', 'delete', name='agencies_temps_delete'),
        # Transportation
        url(r'^employees/update/details/transportation/(?P<identifier>\d+)/?$', 'form_transportation', name='agencies_temps_edit_transportation'),
        # Assignment Restrictions
        url(r'^employees/update/details/assignment-restrictions/(?P<identifier>\d+)/?$', 'assignment_restrictions_list', name='agencies_temps_assignment_restrictions_list'),
        url(r'^employees/update/details/assignment-restrictions/create/(?P<user_id>\d+)/(?P<by_who>\w+)/$', 'assignment_restrictions_form', name='agencies_temps_assignment_restrictions_add'),
        url(r'^employees/update/details/assignment-restrictions/edit/(?P<user_id>\d+)/(?P<identifier>\d+)/$', 'assignment_restrictions_form', name='agencies_temps_assignment_restrictions_edit'),
        url(r'^employees/update/details/assignment-restrictions/delete/(?P<identifier>\d+)/?$', 'assignment_restrictions_delete', name='agencies_temps_assignment_restrictions_delete'),
        # Electronic Pay
        url(r'^employees/update/details/electronic-pay/(?P<identifier>\d+)/?$', 'electronic_pay_form', name='agencies_temps_edit_electronic_pay'),
)

urlpatterns += patterns('agencies.views.agencies_views',
        url(r'^administration/interest-codes$', 'interest_codes_listing', name='agencies_interest_codes_listing'),
        url(r'^administration/interest-codes/create$', 'interest_codes_form', name='agencies_interest_codes_add'),
        url(r'^administration/interest-codes/update/(?P<identifier>\d+)/?$', 'interest_codes_form', name='agencies_interest_codes_listing_edit'),
)

urlpatterns += patterns('agencies.views.pay_setup',
        # Adjustments
        url(r'^employees/pay-setup/adjustments/(?P<identifier>\d+)/?$', 'adjustments_listing', name='agencies_temps_pay_setup_adjustments_list'),
        url(r'^employees/pay-setup/adjustments/create/(?P<user_id>\d+)/$', 'adjustments_form', name='agencies_temps_pay_setup_adjustments_add'),
        url(r'^employees/pay-setup/adjustments/edit/(?P<user_id>\d+)/(?P<identifier>\d+)/$', 'adjustments_form', name='agencies_temps_pay_setup_adjustments_edit'),
        url(r'^employees/pay-setup/adjustments/delete/(?P<adjustment_id>\d+)/$', 'adjustments_delete', name='agencies_temps_pay_setup_adjustments_delete'),
        # Adjustments Rules
        url(r'^employees/pay-setup/adjustments/(?P<user_id>\d+)/(?P<adjustment_id>\d+)/rules/$', 'adjustment_rules_form', name='agencies_temps_pay_setup_adjustment_rules_form'),
        # url(r'^employees/pay-setup/adjustments/edit/(?P<user_id>\d+)/(?P<identifier>\d+)/$', 'adjustments_rule_form', name='agencies_temps_pay_setup_adjustments_rule_edit'),
)

urlpatterns += patterns('agencies.views.customers',
        url(r'^customers/$', 'list', name='agencies_customers_list'),
        url(r'^customers/backtosearch/$', 'backtosearch', name='agencies_customers_backtosearch'),
        url(r'^customers/create$', 'create', name='agencies_customers_create'),
        url(r'^customers/update/(?P<identifier>\d+)/?$', 'update', name='agencies_customers_update'),
        url(r'^customers/billingsetup/(?P<identifier>\d+)/?$', 'billingsetup', name='agencies_customers_billingsetup'),
        url(r'^customers/creditpayroll/(?P<identifier>\d+)/?$', 'creditpayroll', name='agencies_customers_creditpayroll'),
        url(r'^customers/misc/(?P<identifier>\d+)/?$', 'misc', name='agencies_customers_misc'),
        url(r'^customers/delete/(?P<identifier>\d+)/?$', 'delete', name='agencies_customers_delete'),
)

urlpatterns += patterns('agencies.views.orders',
        url(r'^orders/$', 'list', name='agencies_orders_list'),
        url(r'^orders/backtosearch/$', 'backtosearch', name='agencies_orders_backtosearch'),
        url(r'^orders/create$', 'create', name='agencies_orders_create'),
        url(r'^orders/update/(?P<identifier>\d+)/?$', 'update', name='agencies_orders_update'),        
        url(r'^orders/delete/(?P<identifier>\d+)/?$', 'delete', name='agencies_orders_delete'),        
        url(r'^orders/assignments/(?P<identifier>\d+)/?$', 'assignments', name='agencies_orders_assignments'),
)

urlpatterns += patterns('agencies.views.assignments',
        url(r'^orders/(?P<orderid>\d+)/assign/(?P<candidateid>\d+)/?$', 'assigncandidate', name='agencies_assignments_assigncandidate'),
        url(r'^orders/(?P<orderid>\d+)/unassign/(?P<assignmentid>\d+)/?$', 'unassign', name='agencies_assignments_unassign'),
        url(r'^orders/(?P<orderid>\d+)/update/(?P<assignmentid>\d+)/?$', 'update', name='agencies_assignments_update'),
)

urlpatterns += patterns('agencies.views.timeentries',
        url(r'^timeentries/$', 'list', name='agencies_timeentries_list'),
        url(r'^timeentries/(?P<identifier>\d+)/?$', 'detail', name='agencies_timeentries_detail'), 
        url(r'^timeentries/update/(?P<identifier>\d+)/?$', 'update', name='agencies_timeentries_update'),
        url(r'^timeentries/approve/(?P<identifier>\d+)/?$', 'approve', name='agencies_timeentries_approve'),
        url(r'^timeentries/runpayroll/(?P<identifier>\d+)/?$', 'runpayroll', name='agencies_timeentries_runpayroll'),
        url(r'^timeentries/runinvoice/(?P<identifier>\d+)/?$', 'runinvoice', name='agencies_timeentries_runinvoice'),
        url(r'^timeentries/backtosearch/$', 'backtosearch', name='agencies_timeentries_backtosearch'),
)

urlpatterns += patterns('agencies.views.incompletetransactions',
        url(r'^incompletetransactions/$', 'list', name='agencies_incompletetransactions_list'),
)

urlpatterns += patterns('agencies.views.checks',
        url(r'^checks/$', 'list', name='agencies_checks_list'),
        url(r'^checks/(?P<identifier>\d+)/?$', 'detail', name='agencies_checks_detail'),
        url(r'^checks/backtosearch/$', 'backtosearch', name='agencies_checks_backtosearch'),
)

urlpatterns += patterns('agencies.views.invoices',
        url(r'^invoices/$', 'list', name='agencies_invoices_list'),
        url(r'^invoices/(?P<identifier>\d+)/?$', 'detail', name='agencies_invoices_detail'),
        url(r'^invoices/backtosearch/$', 'backtosearch', name='agencies_invoices_backtosearch'),
)

urlpatterns += patterns('agencies.views.payroll',
        url(r'^payroll/start/$', 'start', name='agencies_payroll_start'),
        url(r'^payroll/createunusedtimecards/$', 'createunusedtimecards', name='agencies_payroll_createunusedtimecards'),
        url(r'^payroll/removeunusedtimecards/$', 'removeunusedtimecards', name='agencies_payroll_removeunusedtimecards'),
        url(r'^payroll/prooftransactions/$', 'prooftransactions', name='agencies_payroll_prooftransactions'),
        url(r'^payroll/payroll/start$', 'payroll_start', name='agencies_payroll_runpayroll'),
        url(r'^payroll/payroll/confirm$', 'payroll_confirm', name='agencies_payroll_confirmpayroll'),
        url(r'^payroll/invoicing/start/$', 'invoicing_start', name='agencies_payroll_runinvoicing'),
        url(r'^payroll/invoicing/confirm/$', 'invoicing_confirm', name='agencies_payroll_confirminvoicing'),
)