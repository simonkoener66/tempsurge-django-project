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
from temps.models import InterestCode
from agencies.forms import OrderSearchFilterFormForAgency, OrderNewFormForAgency, OrderUpdateFormForAgency

# Order Search
@group_required('agencies')
def list(request):
	
	#Backup URL with filter criterias
	request.session['orders_search_url'] = request.get_full_path()

	filter_form = OrderSearchFilterFormForAgency(request.GET)

	# Search Query
	query = dict()

	# Customer Name
	if request.GET.get('customer_name'):
		query['customerdepartment__customer__customername__icontains'] = request.GET['customer_name']
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
	return render(request, 'agencies/orders/list.html', {
		'filter_form': filter_form,
		'orders': orders,
		'query_string': query_string
	})


# Back to Order Search Page
@group_required('agencies')
def backtosearch(request):

	url = request.session.get('orders_search_url')
	return redirect(url)


# Order Details
@group_required('agencies')
def update(request, identifier=None):
	
	order = get_object_or_404(WorkOrder.objects.filter(), id=identifier)
	
	if request.method == 'POST':
		order_form = OrderUpdateFormForAgency(request.POST, instance=order)

		if order_form.is_valid():
			of = order_form.save(commit=False)			

			order_form.save_m2m()

			of.save()
			messages.success(request, 'Order #' + identifier + ' has been successfully updated.', extra_tags="order")
			return redirect('agencies_orders_backtosearch')

	else:
		order_form = OrderUpdateFormForAgency(instance=order)

	return render(request, 'agencies/orders/update.html', {
		'customer': order.customerdepartment.customer,
		'order': order,
		'order_form': order_form,
		'identifier': identifier
	})


# Order New
@group_required('agencies')
def create(request, identifier=None):

	order = None

	if request.method == 'POST':
		order_form = OrderNewFormForAgency(request.POST, instance=order, user=request.user)		
		if order_form.is_valid():			
			of = order_form.save(commit=False)
			of.capacity_assigned = 0			
			of.save()

			order = get_object_or_404(WorkOrder, pk=of.id)
			for ic in order.customerdepartment.customer.interest_codes.all():
				order.interest_codes.add(ic)
			order.save()

			return redirect('agencies_orders_update', identifier=of.id)			
	else:
		order_form = OrderNewFormForAgency(instance=order, user=request.user)

	return render(request, 'agencies/orders/create.html', {
		'order': order,
		'order_form': order_form,
		'identifier': identifier
	})

# Order Delete
@group_required('agencies')
def delete(request, identifier):
	order = get_object_or_404(WorkOrder, pk=identifier)
	order.delete()
	messages.success(request, 'The order has been successfully deleted.', extra_tags="order")
	return redirect('agencies_orders_backtosearch')	

# Order's Assignments
@group_required('agencies')
def assignments(request, identifier):
	order = get_object_or_404(WorkOrder.objects.filter(), id=identifier)

	query = dict()
	query['temp__interest_codes__in'] = order.interest_codes.all()

	candidates = User.objects.filter(
		groups__name='Temps',
		userprofile__agency=request.user.userprofile.agency,
		**query
	)

	query = dict()
	query['order__id'] = identifier
	assignments = Assignment.objects.filter(
		**query
	)

	employees = []
	for assignment in assignments:
		employees.append(assignment.employee)

	return render(request, 'agencies/orders/assignments.html',
		{
			'identifier': identifier,
			'order': order,
			'candidates': candidates,
			'assignments': assignments,
			'employees': employees,
		}
	)