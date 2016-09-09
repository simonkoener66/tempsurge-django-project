import datetime
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.forms import extras
from accounts.models import UserProfile
from temps.models import Temp
from accounts.geo.models import City
from accounts.geo.widgets import CityChoiceWidget
from mptt.forms import TreeNodeMultipleChoiceField
from employers.models import Customer, CustomerDepartment, WorkOrder
from agencies.models import Branch, TimeEntry
from django.utils.translation import ugettext_lazy as _


def TimeEntrySearchFormFactory(user):

    orders = WorkOrder.objects.filter(customerdepartment__customer__user__id=user.id)
    class TimeEntrySearchOrderForm(forms.Form):
        order = forms.ModelChoiceField(queryset=orders, empty_label='All Orders')

    return TimeEntrySearchOrderForm
    
def TransactionSearchFormFactory(user):

    orders = WorkOrder.objects.filter(customerdepartment__customer__user__id=user.id)
    class TransactionSearchOrderForm(forms.Form):
        order = forms.ModelChoiceField(queryset=orders, empty_label='All Orders')

    return TransactionSearchOrderForm

class TransactionSearchForm(forms.Form):
	today = datetime.date.today()
	idx = today.weekday()
	sun = today + datetime.timedelta(6-idx)
	sundays = []
	sundays.append(['---','All Weekends'])
	while sun.year==today.year:
		sundays.append([sun,sun])
		sun = sun - datetime.timedelta(7)

	weekends = forms.ChoiceField(choices=sundays)

class OrderSearchFormByCustomer(forms.Form):
	order_id = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Order ID', 'class': 'input-medium'}))
	status = forms.ChoiceField(choices=(
		('all', 'All'),
		('Unfilled', 'Unfilled'),
		('Filled', 'Filled'),
		('Closed', 'Closed'),		
	))
	active = forms.ChoiceField(choices=(
		('all', 'All'),
		('active', 'Active'),
		('inactive', 'Inactive'),		
	))
	rep = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Agencies'), empty_label='All Reps')
	branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='All Branches')


class OrderNewForm(forms.ModelForm):

	class Meta:
		model = WorkOrder
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(OrderNewForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['customerdepartment'] = forms.ModelChoiceField(required=True, queryset=CustomerDepartment.objects.filter(customer__user__id=user.id))
			self.fields['customerdepartment'].required = True
			self.fields['customerdepartment'].label = 'Department'


class OrderForm(forms.ModelForm):

	class Meta:
		model = WorkOrder
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance:			
			self.fields['customerdepartment'] = forms.ModelChoiceField(required=True, queryset=CustomerDepartment.objects.filter(customer__user__id=instance.customerdepartment.customer.user.id))
			self.fields['customerdepartment'].label = 'Department'
			self.fields['directions'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))

			self.fields['pay_rate'].label = 'Pay Rate'
			self.fields['bill_rate'].label = 'Bill Rate'
			self.fields['overtime_bill'].label = 'Overtime Bill'
			self.fields['doubletime_bill'].label = 'Doubletime Bill'
			self.fields['overtime_plan'].label = 'Overtime Plan'
			self.fields['ot_factor'].label = 'OT FACTOR'
			self.fields['multiplier'].label = 'Multiplier'
			self.fields['pay_periods'].label = 'Pay Periods'

			self.fields['capacity_required'].label = 'Required'
			self.fields['capacity_assigned'].label = 'Assigned'
			self.fields['workday_sunday'].label = 'Sun'
			self.fields['workday_monday'].label = 'Mon'
			self.fields['workday_tuesday'].label = 'Tue'
			self.fields['workday_wednesday'].label = 'Wed'
			self.fields['workday_thursday'].label = 'Thu'
			self.fields['workday_friday'].label = 'Fri'
			self.fields['workday_saturday'].label = 'Sat'

			self.fields['rep'] = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Agencies'))
			self.fields['notes'] = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
			self.fields['description'] = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
			self.fields['safety_notes'] = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
			self.fields['shift_notes'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))


			self.fields['customerdepartment'].required = True
			self.fields['pay_rate'].required = True
			self.fields['bill_rate'].required = True
			self.fields['order_type'].required = True
			self.fields['job_title'].required = True
			self.fields['status'].required = True
			self.fields['rep'].required = True
			self.fields['branch'].required = True

			self.fields['capacity_assigned'].widget.attrs['readonly'] = True


class TimeentryForm(forms.ModelForm):

	class Meta:
		model = TimeEntry
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super(TimeentryForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance:
			self.fields['pay_roll'] = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
