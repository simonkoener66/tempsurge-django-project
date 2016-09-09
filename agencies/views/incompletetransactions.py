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
from agencies.models import TimeEntry
from agencies.forms import IncompleteTransactionSearchFilterFormForAgency


# Incomplete Transaction Search Page
@group_required('agencies')
def list(request):

	filter_form = IncompleteTransactionSearchFilterFormForAgency(request.GET)

	# Search Query
	query = dict()
	if request.GET.get('order'):
		query['assignment__order__id'] = request.GET['order']
	if request.GET.get('weekends') is not None and request.GET.get('weekends') != '---':
		query['we_date__icontains'] = request.GET.get('weekends')

	transaction_list = TimeEntry.objects.filter(
        **query
    )

    # Pagination
	paginator = Paginator(transaction_list, 50)

	page = request.GET.get('page')
	try:
		transactions = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		transactions = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		transactions = paginator.page(paginator.num_pages)

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

	return render(request, 'agencies/incompletetransactions/list.html', {
		'transactions': transactions,		
		'filter_form': filter_form,
		'query_string': query_string
	})


