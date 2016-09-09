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
from agencies.forms import AssignmentNewFormForAgency, AssignmentUpdateFormForAgency

# Assign Candidate to Order
@group_required('agencies')
def assigncandidate(request, orderid=None, candidateid=None):

	order = get_object_or_404(WorkOrder.objects.filter(), id=orderid)
	candidate = get_object_or_404(User.objects.filter(), id=candidateid)
	assignment = None

	if request.method == 'POST':
		assignment_form = AssignmentNewFormForAgency(request.POST, instance=assignment, order=order, user=request.user)		
		if assignment_form.is_valid():			
			af = assignment_form.save(commit=False)
			af.order = order
			af.employee = candidate.temp
			af.status = 'Open'
			af.job_title = order.job_title
			af.expected_start_date = order.start_date
			af.expected_end_date = order.end_date
			af.shift = order.shift
			af.start_time = order.start_time
			af.end_time = order.end_time
			af.shift_notes = order.shift_notes
			af.workday_sunday = order.workday_sunday
			af.workday_monday = order.workday_monday
			af.workday_tuesday = order.workday_tuesday
			af.workday_wednesday = order.workday_wednesday
			af.workday_thursday = order.workday_thursday
			af.workday_friday = order.workday_friday
			af.workday_saturday = order.workday_saturday
			af.multiplier = order.multiplier
			af.ot_factor = order.ot_factor
			af.pay_rate = order.pay_rate
			af.overtime_pay = order.ot_pay
			af.doubletime_pay = order.dt_pay
			af.bill_rate = order.bill_rate
			af.overtime_bill = order.overtime_bill
			af.doubletime_bill = order.doubletime_bill
			af.do_not_auto_close = order.do_not_auto_close

			af.save()

			order.capacity_assigned = order.capacity_assigned + 1
			order.save()
			messages.success(request, 'The candidate has been successfully assigned.', extra_tags="assignment")

		return redirect('agencies_orders_assignments', identifier=order.id)
	else:
		assignment_form = AssignmentNewFormForAgency(instance=assignment, order=order, user=request.user)

	return render(request, 'agencies/assignments/assigncandidate.html', {
		'assignment': assignment,
		'order': order,
		'candidate': candidate,
		'assignment_form': assignment_form,
	})


# Unassign employee from order
@group_required('agencies')
def unassign(request, orderid=None, assignmentid=None):
	assignment = get_object_or_404(Assignment, pk=assignmentid)
	order = assignment.order

	assignment.delete()

	order.capacity_assigned = order.capacity_assigned - 1
	order.save()

	messages.success(request, 'The assignment has been successfully deleted.', extra_tags="assignment")
	return redirect('agencies_orders_assignments', identifier=orderid)

# Update assignment
@group_required('agencies')
def update(request, orderid=None, assignmentid=None):
	
	order = get_object_or_404(WorkOrder.objects.filter(), id=orderid)
	assignment = get_object_or_404(Assignment.objects.filter(), id=assignmentid)
	employee = assignment.employee
	
	if request.method == 'POST':
		assignment_form = AssignmentUpdateFormForAgency(request.POST, instance=assignment)

		if assignment_form.is_valid():
			af = assignment_form.save(commit=False)
			af.order = order
			af.employee = employee
			af.save()
			messages.success(request, 'The assignment has been successfully updated.', extra_tags="assignment")
			return redirect('agencies_orders_assignments', identifier=orderid)

	else:
		assignment_form = AssignmentUpdateFormForAgency(instance=assignment)

	return render(request, 'agencies/assignments/update.html', {
		'order': order,
		'assignment': assignment,
		'assignment_form': assignment_form,
	})	