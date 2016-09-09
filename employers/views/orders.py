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
from employers.models import WorkOrder, WorkOrderType, JobTitle, Assignment, BusinessCode
from employers.forms import OrderSearchFormByCustomer, OrderForm, OrderNewForm

@group_required('employers')
def list(request):
	
	search_form = OrderSearchFormByCustomer(request.GET)

	query = dict()

	query['customerdepartment__customer__user__id'] = request.user.id;

	# Order ID
	if request.GET.get('order_id'):
		query['id__icontains'] = request.GET['order_id']

	# Status
	if request.GET.get('status') is not None and request.GET.get('status') != 'all':
		query['status'] = request.GET['status']

	# Active
	if request.GET.get('active') == 'active':
		query['active'] = True
	elif request.GET.get('active') == 'inactive':
		query['active'] = False

	# Rep
	if request.GET.get('rep'):
		query['rep'] = request.GET['rep']

	# Branch
	if request.GET.get('branch'):
		query['branch'] = request.GET['branch']
	
	order_list = WorkOrder.objects.filter(
		**query
	)

	# Pagination
	paginator = Paginator(order_list, 50)

	page = request.GET.get('page')
	try:
		orders = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		orders = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		orders = paginator.page(paginator.num_pages)

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

	# Serve Template
	return render(request, 'orders/list.html', {
		'search_form': search_form,
		'orders': orders,
		'query_string': query_string
	})


@group_required('employers')
def detail(request, identifier):
	order = get_object_or_404(WorkOrder.objects.filter(), id=identifier)

	query = dict()
	query['order__id'] = identifier
	assignments = Assignment.objects.filter(
		**query
	)

	return render(request, 'orders/detail.html',
		{
			'order': order,
			'assignments': assignments,
		}
	)


@group_required('employers')
def update(request, identifier=None):
	
	order = get_object_or_404(WorkOrder.objects.filter(), id=identifier)
	
	if request.method == 'POST':
		order_form = OrderForm(request.POST, instance=order)

		if order_form.is_valid():
			of = order_form.save(commit=False)			
			of.save()
			messages.success(request, 'The order details has been successfully saved.', extra_tags="order")
			return redirect('employers_orders_list')

	else:
		order_form = OrderForm(instance=order)

	return render(request, 'orders/update.html', {
		'order': order,
		'order_form': order_form,
		'identifier': identifier
	})


@group_required('employers')
def create(request, identifier=None):

	order = None

	if request.method == 'POST':
		order_form = OrderNewForm(request.POST, instance=order, user=request.user)		
		if order_form.is_valid():			
			of = order_form.save(commit=False)
			of.capacity_assigned = 0
			of.save()			
			return redirect('employers_orders_update', identifier=of.id)			
	else:
		order_form = OrderNewForm(instance=order, user=request.user)

	return render(request, 'orders/create.html', {
		'order': order,
		'order_form': order_form,
		'identifier': identifier
	})

@group_required('employers')
def delete(request, identifier):
	order = get_object_or_404(WorkOrder, pk=identifier)
	order.delete()
	messages.success(request, 'The order has been successfully deleted.', extra_tags="order")
	return redirect('employers_orders_list')	