"""
This is for Customer Management: Customer Search, Details, Update, Delete
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
from employers.models import Customer, CustomerDepartment, CustomerBillingInformation, CustomerCreditPayrollInformation, CustomerMiscInformation
from temps.models import AssignmentRestriction, ACHBankAccount, PayCardAccount
from agencies.forms import SearchUserForm, SearchTempForm, SearchBranchForm, SearchRepForm, SearchInterestCodeForm
from agencies.forms import CustomerSearchFilterForm, CustomerNewForm, CustomerUpdateForm, CustomerBillingInformationForm, CustomerCreditPayrollInformationForm, CustomerMiscInformationForm
from accounts.forms import UserForm, ProfileForm
from temps.forms import TempForm, TransportationForm, AssignmentRestrictionForm, ElectronicPaymentForm, ACHBankAccountForm, PayCardAccountForm


# Customer Search
@group_required('agencies')
def list(request):

	#Backup URL with filter criterias
	request.session['customers_search_url'] = request.get_full_path()

	filter_form = CustomerSearchFilterForm(request.GET)

	#Search Query
	query = dict()

	# Customer Name
	if request.GET.get('customer_name'):
		query['customer__customername__icontains'] = request.GET['customer_name']
	# Customer ID
	if request.GET.get('customer_id'):
		query['customer__id__icontains'] = request.GET['customer_id']
	# Active/All Records
	if request.GET.get('active') is None or request.GET.get('active') == 'active':
		query['active'] = True
	# Include Departments
	if request.GET.get('include_dept') is None or request.GET.get('include_dept') == False:
		query['parentdep__isnull'] = True
	# Sales Manager
	if request.GET.get('accountmanager'):
		query['customer__accountmanager'] = request.GET['accountmanager']
    # Branch
	if request.GET.get('branch'):
		query['customer__branch__id'] = request.GET['branch']

	dept_list = CustomerDepartment.objects.filter(
		**query
	)

	# Pagination
	paginator = Paginator(dept_list, 50)

	page = request.GET.get('page')
	try:
		depts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		depts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		depts = paginator.page(paginator.num_pages)

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
	return render(request, 'agencies/customers/list.html', {
		'depts': depts,
		'filter_form': filter_form,
		'query_string': query_string
	})


#Back to Customer Search Page
@group_required('agencies')
def backtosearch(request):

	url = request.session.get('customers_search_url')
	return redirect(url)


#Customer Create
@group_required('agencies')
def create(request, identifier=None):
	customer = None
	user = None
	profile = None

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
		customer_form = CustomerNewForm(request.POST, instance=customer)

		if user_form.is_valid() and profile_form.is_valid() and customer_form.is_valid():
			uf = user_form.save(commit=False)		
			uf.save()

			g = Group.objects.get(name='Employer Admin')
			g.user_set.add(uf)

			pf = profile_form.save(commit=False)
			pf.agency = request.user.userprofile.agency
			pf.user = uf
			pf.save()

			cf = customer_form.save(commit=False)
			cf.user = uf

			cf.activedate = datetime.now()

			cf.save()

			primary_dept = CustomerDepartment()
			primary_dept.customer = cf
			primary_dept.depname = 'Primary'
			primary_dept.activedate = datetime.now()
			primary_dept.save()

			messages.success(request, 'New customer has been successfully created.', extra_tags="customer")
			return redirect('agencies_customers_backtosearch')

	else:
		customer_form = CustomerNewForm(instance=customer)
		user_form = UserForm(instance=user, initial={'first_name':'aa'+datetime.now().strftime('%m%d%Y-%y%s'), 'last_name':'aa'+datetime.now().strftime('%m%d%Y-%y%s'), 'username': 'aa'+datetime.now().strftime('%m%d%Y-%y%s') })
		profile_form = ProfileForm(instance=profile)


	return render(request, 'agencies/customers/create.html', {
		'identifier': identifier,
		'customer_form': customer_form,
		'user_form': user_form,
		'profile_form': profile_form,
	})


# Customer Details
@group_required('agencies')
def update(request, identifier):
	customer = get_object_or_404(Customer.objects.filter(), id=identifier)
	user = customer.user
	profile = customer.user.userprofile

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
		customer_form = CustomerUpdateForm(request.POST, instance=customer)

		if user_form.is_valid() and profile_form.is_valid() and customer_form.is_valid():
			uf = user_form.save(commit=False)		
			uf.save()

			g = Group.objects.get(name='Employer Admin')
			g.user_set.add(uf)

			pf = profile_form.save(commit=False)
			pf.agency = request.user.userprofile.agency
			pf.user = uf
			pf.save()

			cf = customer_form.save(commit=False)
			cf.user = uf

			customer_form.save_m2m()

			if not identifier:
				uf.activedate = datetime.now()

			cf.save()

			messages.success(request, 'Customer #' + identifier + ' has been successfully updated.', extra_tags="customer")
			return redirect('agencies_customers_backtosearch')

	else:
		customer_form = CustomerUpdateForm(instance=customer)
		user_form = UserForm(instance=user, initial={'first_name':'aa'+datetime.now().strftime('%m%d%Y-%y%s'), 'last_name':'aa'+datetime.now().strftime('%m%d%Y-%y%s'), 'username': 'aa'+datetime.now().strftime('%m%d%Y-%y%s') })
		profile_form = ProfileForm(instance=profile)


	return render(request, 'agencies/customers/update.html', {
		'identifier': identifier,
		'customer_form': customer_form,
		'user_form': user_form,
		'profile_form': profile_form,
	})

# Customer Billing Setup
@group_required('agencies')
def billingsetup(request, identifier):
	customer = get_object_or_404(Customer, pk=identifier)
	user = customer.user
	if hasattr(user, 'customerbillinginformation'):
		billing = user.customerbillinginformation
	else:
		billing = CustomerBillingInformation()

	billing.user = user

	if request.method == 'POST':

		billing_form = CustomerBillingInformationForm(request.POST, instance=billing)
		if billing_form.is_valid():
			bf = billing_form.save(commit=False)
			bf.save()
			messages.success(request, "Customer #" + identifier + "'s billing information has been successfully setted up.", extra_tags="customer")
			return redirect('agencies_customers_backtosearch')

	else:
		billing_form = CustomerBillingInformationForm(instance = billing)

	return render(request, 'agencies/customers/billingsetup.html', {
		'identifier': identifier,
		'billing_form': billing_form,
	})


# Customer Credit Payroll Information Update
@group_required('agencies')
def creditpayroll(request, identifier):
	customer = get_object_or_404(Customer, pk=identifier)
	user = customer.user
	if hasattr(user, 'customercreditpayrollinformation'):
		cp = user.customercreditpayrollinformation
	else:
		cp = CustomerCreditPayrollInformation()

	cp.user = user

	if request.method == 'POST':
		creditpayroll_form = CustomerCreditPayrollInformationForm(request.POST, instance=cp)
		if creditpayroll_form.is_valid():
			cf = creditpayroll_form.save(commit=False)
			cf.save()
			messages.success(request, "Customer #" + identifier + "'s credit and payroll have been successfully setted up.", extra_tags="customer")
			return redirect('agencies_customers_backtosearch')

	else:
		creditpayroll_form = CustomerCreditPayrollInformationForm(instance = cp)

	return render(request, 'agencies/customers/creditpayroll.html', {
		'identifier': identifier,
		'creditpayroll_form': creditpayroll_form,
	})


# Customer Misc Informaition Update
@group_required('agencies')
def misc(request, identifier):
	customer = get_object_or_404(Customer, pk=identifier)
	user = customer.user
	if hasattr(user, 'customermiscinformation'):
		cmisc = user.customermiscinformation
	else:
		cmisc = CustomerMiscInformation()

	cmisc.user = user

	if request.method == 'POST':
		misc_form = CustomerMiscInformationForm(request.POST, instance=cmisc)
		if misc_form.is_valid():
			cf = misc_form.save(commit=False)
			cf.save()
			messages.success(request, "Customer #" + identifier + "'s miscellaneous and credit card details have been successfully setted up.", extra_tags="customer")
			return redirect('agencies_customers_backtosearch')

	else:
		misc_form = CustomerMiscInformationForm(instance = cmisc)

	return render(request, 'agencies/customers/misc.html', {
		'identifier': identifier,
		'misc_form': misc_form,
	})


# Customer Delete
@group_required('agencies')	
def delete(request, identifier):
	customer = get_object_or_404(Customer, pk=identifier)
	customer.user.userprofile.delete()
	customer.user.delete()
	customer.delete()
	messages.success(request, 'The customer has been successfully deleted.', extra_tags="customer")
	return redirect('agencies_customers_backtosearch')	