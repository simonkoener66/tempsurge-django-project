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

@group_required('employers')
def unassign(request, orderid=None, assignmentid=None):
	assignment = get_object_or_404(Assignment, pk=assignmentid)
	assignment.delete()
	messages.success(request, 'The assignment has been successfully deleted.', extra_tags="assignment")
	return redirect('employers_orders_detail', identifier=orderid)

@group_required('employers')
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
			return redirect('agencies_orders_detail', identifier=orderid)

	else:
		assignment_form = AssignmentUpdateFormForAgency(instance=assignment)

	return render(request, 'assignments/update.html', {
		'order': order,
		'assignment': assignment,
		'assignment_form': assignment_form,
	})	