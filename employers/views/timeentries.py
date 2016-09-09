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
from employers.forms import TimeentryForm
from agencies.models import TimeEntry
from agencies.forms import TimeEntrySearchFilterFormForAgency
from employers.forms import TimeEntrySearchFormFactory

@group_required('employers')
def list(request):

	status_form  = TimeEntrySearchFilterForm(request.GET)
	
	orderformclass = TimeEntrySearchFormFactory(request.user)
	order_form = orderformclass()

	query = dict()

	query['assignment__order__customerdepartment__customer__user__id'] = request.user.id

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

	get_request = request.GET.copy()

	if 'page' in get_request:
		del get_request['page']

	url_encoded = urllib.urlencode(get_request)

	query_string = '?' + url_encoded

	if url_encoded:
		query_string += "&"

	if not query_string:
		query_string = '?'

    # Serve Template
	return render(request, 'timeentries/list.html', {
		'timeentries': timeentries,
		'status_form': status_form,
		'order_form': order_form,
		'query_string': query_string
	})

@group_required('employers')
def detail(request, identifier):
    timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)

    return render(request, 'timeentries/detail.html',
        {
            'timeentry': timeentry,
        }
    )


@group_required('employers')
def approve(request, identifier):
	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	timeentry.status_id = 3
	timeentry.save()

	messages.success(request, "The Time Entry #" + str(identifier) + " has been proofed", extra_tags="timeentry")

	return redirect('employers_timeentries_list')


@group_required('employers')
def update(request, identifier=None):
	
	timeentry = get_object_or_404(TimeEntry.objects.filter(), id=identifier)
	
	if request.method == 'POST':
		timeentry_form = TimeentryForm(request.POST, instance=timeentry)

		if timeentry_form.is_valid():
			tf = timeentry_form.save(commit=False)	
			tf.adj_gross = 0
			tf.adj_net = 0		
			if tf.status_id == 1:
				tf.status_id = 2
			tf.save()
			messages.success(request, 'The Time Entry #' + str(identifier) + ' has been successfully updated.', extra_tags="timeentry")
			return redirect('employers_timeentries_list')

	else:
		timeentry_form = TimeentryForm(instance=timeentry)

	return render(request, 'timeentries/update.html', {
		'timeentry': timeentry,
		'timeentry_form': timeentry_form,
		'identifier': identifier
	})