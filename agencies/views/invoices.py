"""
Note that this particular filename contain _views to avoid overriding 'temps' module containing the file!
"""

import operator
import urllib
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import group_required
from temps.models import AssignmentRestriction, ACHBankAccount, PayCardAccount
from agencies.forms import InvoiceSearchFilterFormForAgency
from agencies.models import TimeEntry, Check, Invoice


# Invoice Search
@group_required('agencies')
def list(request):
	#Backup Search URL with filter criterias
	request.session['invoices_search_url'] = request.get_full_path()

	filter_form  = InvoiceSearchFilterFormForAgency(request.GET)

	#Search Query
	query = dict()
	if request.GET.get('weekends') is not None and request.GET.get('weekends') != '---':
		query['timeentry__we_date__icontains'] = request.GET.get('weekends')
	if request.GET.get('employee_first_name'):
		query['timeentry__assignment__employee__user__first_name__icontains'] = request.GET['employee_first_name']
	if request.GET.get('employee_last_name'):
		query['timeentry__assignment__employee__user__last_name__icontains'] = request.GET['employee_last_name']
	if request.GET.get('customer_name'):
		query['timeentry__assignment__order__customerdepartment__customer__customername__icontains'] = request.GET['customer_name']
	
	invoice_list = Invoice.objects.filter(
        **query
    )

    # Pagination
	paginator = Paginator(invoice_list, 50)

	page = request.GET.get('page')
	try:
		invoices = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		invoices = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		invoices = paginator.page(paginator.num_pages)

    # Query String
    # Avoid &page=N&page=N&page=N... when going to next pages
	get_request = request.GET.copy()

	if 'page' in get_request:
		del get_request['page']

	url_encoded = urllib.urlencode(get_request)

	query_string = '?' + url_encoded

	if url_encoded:
		query_string += "&"

	if not query_string:
		query_string = '?'

	return render(request, 'agencies/invoices/list.html', {
		'invoices': invoices,		
		'query_string': query_string,
		'filter_form': filter_form,
	})

#Back to Search URL
@group_required('agencies')
def backtosearch(request):

	url = request.session.get('invoices_search_url')
	return redirect(url)


#Invoice Details
@group_required('agencies')
def detail(request, identifier):
	invoice = get_object_or_404(Invoice.objects.filter(), id=identifier)

	bill_rate = invoice.timeentry.bill_rate if invoice.timeentry.bill_rate is not None else 0
	hours_regular = invoice.timeentry.hours_regular if invoice.timeentry.hours_regular is not None else 0
	regular_amount = bill_rate * hours_regular

	ot_bill = invoice.timeentry.ot_bill if invoice.timeentry.ot_bill is not None else 0
	hours_overtime = invoice.timeentry.hours_overtime if invoice.timeentry.hours_overtime is not None else 0
	overtime_amount = ot_bill * hours_overtime

	dt_bill = invoice.timeentry.dt_bill if invoice.timeentry.dt_bill is not None else 0
	hours_doubletime = invoice.timeentry.hours_doubletime if invoice.timeentry.hours_doubletime is not None else 0
	doubletime_amount = dt_bill * hours_doubletime

	tax = invoice.tax

	gross = invoice.gross

	return render(request, 'agencies/invoices/detail.html',
		{
			'invoice': invoice,
			'identifier': identifier,
			'bill_rate': bill_rate,
			'hours_regular': hours_regular,
			'regular_amount': regular_amount,
			'ot_bill': ot_bill,
			'hours_overtime': hours_overtime,
			'overtime_amount': overtime_amount,
			'dt_bill': dt_bill,
			'hours_doubletime': hours_doubletime,
			'doubletime_amount': doubletime_amount,
			'tax': tax,
			'gross': gross,
		}
	)