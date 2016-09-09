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
from temps.models import AssignmentRestriction, ACHBankAccount, PayCardAccount
from agencies.forms import SearchUserForm, SearchTempForm, SearchBranchForm, SearchRepForm, SearchInterestCodeForm
from accounts.forms import UserForm, ProfileForm
from temps.forms import TempForm, TransportationForm, AssignmentRestrictionForm, ElectronicPaymentForm, ACHBankAccountForm, PayCardAccountForm
from agencies.models import TimeEntry, Check, Invoice
from employers.models import Assignment


# Payroll & Invoicing Start Page
@group_required('agencies')
def start(request):

	query = dict()
	
	unused_timeentries = TimeEntry.objects.filter(status__id=1)	
	claimed_timeentries = TimeEntry.objects.filter(status__id=2)
	proofed_timeentries = TimeEntry.objects.filter(status__id=3)
	paid_timeentries = TimeEntry.objects.filter(status__id=4)

	open_assignments = Assignment.objects.filter(status='Open')

	return render(request, 'agencies/payroll/start.html',
		{
			'number_of_open_assignments': len(open_assignments),
			'open_assignments': open_assignments,
			'number_of_unused_timeentries': len(unused_timeentries),
			'unused_timeentries': unused_timeentries,
			'number_of_claimed_timeentries': len(claimed_timeentries),
			'claimed_timeentries': claimed_timeentries,
			'number_of_proofed_timeentries': len(proofed_timeentries),
			'proofed_timeentries': proofed_timeentries,
			'number_of_paid_timeentries': len(paid_timeentries),
			'paid_timeentries': paid_timeentries,
		}
	)

# Create Time Entries from Open Assignments
@group_required('agencies')
def createunusedtimecards(request):

	query = dict()
	query['status'] = 'Open'
	assignments = Assignment.objects.filter(**query)

	sz = 0

	for assignment in assignments:
		today = datetime.date.today()
		idx = today.weekday()
		sun = today + datetime.timedelta(6-idx)

		query = dict()
		query['assignment__id'] = assignment.id
		query['we_bill'] = sun
		te = TimeEntry.objects.filter(**query)

		if len(te)==0:
			timeentry = TimeEntry(
				assignment=assignment, 

				we_bill=sun,
				we_date=sun, 

				salary_approved=False,

				bill_rate = assignment.bill_rate,
				pay_rate = assignment.pay_rate,
				ot_bill = assignment.overtime_bill,
				dt_bill = assignment.doubletime_bill,
				ot_pay = assignment.overtime_pay,
				dt_pay = assignment.doubletime_pay,

				status_id=1, 				
			)
			timeentry.save()
			sz = sz + 1

	messages.success(request, str(sz) + ' time entries have been newly created', extra_tags="timeentry")

	return redirect('agencies_timeentries_list')

# Remove Unused Time Entries
@group_required('agencies')
def removeunusedtimecards(request):

	query = dict()
	query['status__id'] = 1
	unused_timeentries = TimeEntry.objects.filter(**query)

	sz = len(unused_timeentries)

	for timeentry in unused_timeentries:
		timeentry.delete()

	messages.success(request, str(sz) + ' unused time entries have been removed', extra_tags="timeentry")

	return redirect('agencies_timeentries_list')

# Proof unproofed transactions
@group_required('agencies')
def prooftransactions(request):
	
	query = dict()
	query['status__id'] = 2
	claimed_timeentries = TimeEntry.objects.filter(**query)

	sz = len(claimed_timeentries)

	for timeentry in claimed_timeentries:
		timeentry.status_id = 3
		timeentry.save()

	messages.success(request, str(sz) + ' time entries have been proofed', extra_tags="timeentry")

	return redirect('agencies_timeentries_list')

# Asks Whether start payroll
@group_required('agencies')
def payroll_start(request):

	proofed_timeentries = TimeEntry.objects.filter(status__id=3)

	return render(request, 'agencies/payroll/payroll_step1.html',
		{
			'count':	len(proofed_timeentries),
			'proofed_timeentries': proofed_timeentries,
		}
	)

# Run payroll
@group_required('agencies')
def payroll_confirm(request):

	proofed_timeentries = TimeEntry.objects.filter(status__id=3)

	for transaction in proofed_timeentries:
		transaction.status_id = 4
		transaction.save()

		check = Check()
		check.timeentry = transaction
		check.checkdate = datetime.date.today()

		check.gross = 0
		if transaction.pay_rate is not None and transaction.hours_regular is not None:
			check.gross = check.gross + transaction.pay_rate * transaction.hours_regular
		if transaction.ot_pay is not None and transaction.hours_overtime is not None:
			check.gross = check.gross + transaction.ot_pay * transaction.hours_overtime
		if transaction.dt_pay is not None and transaction.hours_doubletime is not None:
			check.gross = check.gross + transaction.dt_pay * transaction.hours_doubletime
		check.tax = 0
		check.net = check.gross - check.tax

		check.save()

	messages.success(request, str(len(proofed_timeentries)) + ' transactions have been paid', extra_tags="timeentry")

	return redirect('agencies_timeentries_list')

# Asks Whether start payroll
@group_required('agencies')
def invoicing_start(request):

	paid_timeentries = TimeEntry.objects.filter(status__id=4)

	return render(request, 'agencies/payroll/invoicing_step1.html',
		{
			'count':	len(paid_timeentries),
			'paid_timeentries': paid_timeentries,
		}
	)

# Run invoicing
@group_required('agencies')
def invoicing_confirm(request):

	paid_timeentries = TimeEntry.objects.filter(status__id=4)

	for transaction in paid_timeentries:
		transaction.status_id = 5
		transaction.save()

		invoice = Invoice()
		invoice.timeentry = transaction
		invoice.invoicedate = datetime.date.today()

		invoice.gross = 0
		if transaction.bill_rate is not None and transaction.hours_regular is not None:
			invoice.gross = invoice.gross + transaction.bill_rate * transaction.hours_regular
		if transaction.ot_bill is not None and transaction.hours_overtime is not None:
			invoice.gross = invoice.gross + transaction.ot_bill * transaction.hours_overtime
		if transaction.dt_bill is not None and transaction.hours_doubletime is not None:
			invoice.gross = invoice.gross + transaction.dt_bill * transaction.hours_doubletime
		invoice.tax = 0
		invoice.net = invoice.gross - invoice.tax
	
		invoice.save()

	messages.success(request, str(len(paid_timeentries)) + ' transactions have been invoiced', extra_tags="timeentry")

	return redirect('agencies_timeentries_list')