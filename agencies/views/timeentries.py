"""
"""

import operator
import urllib
from datetime import datetime
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import group_required
from agencies.models import TimeEntry, Check, Invoice
from temps.models import AssignmentRestriction, ACHBankAccount, PayCardAccount
from agencies.forms import TimeEntrySearchFilterFormForAgency, TimeEntryUpdateFormForAgency

# Time Entry Search
@group_required('agencies')
def list(request):

	#Backup Search URL with filter criterias
	request.session['timeentries_search_url'] = request.get_full_path()

	filter_form  = TimeEntrySearchFilterFormForAgency(request.GET)
	
	# Search Query
	query = dict()
	if request.GET.get('status'):
		query['status'] = request.GET['status']
	if request.GET.get('order'):
		query['assignment__order__id'] = request.GET['order']
	if request.GET.get('weekends') is not None and request.GET.get('weekends') != '---':
		query['we_date__icontains'] = request.GET.get('weekends')

	timeentry_list = TimeEntry.objects.filter(
        **query
    )

    # Pagination
	paginator = Paginator(timeentry_list, 50)

	page = request.GET.get('page')
	try:
		timeentries = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		timeentries = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		timeentries = paginator.page(paginator.num_pages)

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

	return render(request, 'agencies/timeentries/list.html', {
		'timeentries': timeentries,
		'filter_form': filter_form,
		'query_string': query_string
	})


# Back to Time Entry Search Page
@group_required('agencies')
def backtosearch(request):

	url = request.session.get('timeentries_search_url')
	return redirect(url)


# Time Entry Details
@group_required('agencies')
def detail(request, identifier):
    timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)

    return render(request, 'agencies/timeentries/detail.html',
        {
        	'identifier': identifier,
            'timeentry': timeentry,
        }
    )


# Time Entry Update
@group_required('employers')
def update(request, identifier=None):
	
	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	
	if request.method == 'POST':
		timeentry_form = TimeEntryUpdateFormForAgency(request.POST, instance=timeentry)

		if timeentry_form.is_valid():
			tf = timeentry_form.save(commit=False)	
			tf.adj_gross = 0
			tf.adj_net = 0		
			if tf.status_id == 1:
				tf.status_id = 2
			tf.save()
			messages.success(request, 'The Time Entry #' + str(identifier) + ' has been successfully updated.', extra_tags="timeentry")
			return redirect('agencies_timeentries_backtosearch')

	else:
		timeentry_form = TimeEntryUpdateFormForAgency(instance=timeentry)

	return render(request, 'agencies/timeentries/update.html', {
		'timeentry': timeentry,
		'timeentry_form': timeentry_form,
		'identifier': identifier,
	})


# Time Entry Proof
@group_required('agencies')
def approve(request, identifier):
	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	timeentry.status_id = 3
	timeentry.save()

	messages.success(request, "The Time Entry #" + str(identifier) + " has been proofed", extra_tags="timeentry")

	return redirect('agencies_timeentries_backtosearch')


# Time Entry Run Payroll
@group_required('agencies')
def runpayroll(request, identifier):

	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	timeentry.status_id = 4
	timeentry.save()

	check = Check()
	check.timeentry = timeentry
	check.checkdate = datetime.date.today()

	check.gross = 0
	if timeentry.pay_rate is not None and timeentry.hours_regular is not None:
		check.gross = check.gross + timeentry.pay_rate * timeentry.hours_regular
	if timeentry.ot_pay is not None and timeentry.hours_overtime is not None:
		check.gross = check.gross + timeentry.ot_pay * timeentry.hours_overtime
	if timeentry.dt_pay is not None and timeentry.hours_doubletime is not None:
		check.gross = check.gross + timeentry.dt_pay * timeentry.hours_doubletime
	check.tax = 0
	check.net = check.gross - check.tax

	check.save()

	messages.success(request, "The Time Entry #" + str(identifier) + " has been paid", extra_tags="timeentry")

	return redirect('agencies_timeentries_backtosearch')


# Time Entry Run Invoicing
@group_required('agencies')
def runinvoice(request, identifier):

	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	timeentry.status_id = 5
	timeentry.save()

	invoice = Invoice()
	invoice.timeentry = timeentry
	invoice.invoicedate = datetime.date.today()

	invoice.gross = 0
	if timeentry.bill_rate is not None and timeentry.hours_regular is not None:
		invoice.gross = invoice.gross + timeentry.bill_rate * timeentry.hours_regular
	if timeentry.ot_bill is not None and timeentry.hours_overtime is not None:
		invoice.gross = invoice.gross + timeentry.ot_bill * timeentry.hours_overtime
	if timeentry.dt_bill is not None and timeentry.hours_doubletime is not None:
		invoice.gross = invoice.gross + timeentry.dt_bill * timeentry.hours_doubletime
	invoice.tax = 0
	invoice.net = invoice.gross - invoice.tax

	invoice.save()

	messages.success(request, "The Time Entry #" + str(identifier) + " has been invoiced", extra_tags="timeentry")

	return redirect('agencies_timeentries_backtosearch')