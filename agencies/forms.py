import datetime
from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from mptt.forms import TreeNodeMultipleChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Field, Div, Fieldset
from agencies.models import Branch
from temps.models import InterestCode, InterestCodeSynonym
from agencies.models import TimeEntry, TimeEntryStatus
from employers.models import Customer, CustomerStatus, WorkOrder, JobTitle, WorkOrderType, CustomerDepartment, BusinessCode, Assignment, CustomerBillingInformation, CustomerCreditPayrollInformation,CustomerMiscInformation


# Temps Management

class SearchUserForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'ID', 'class': 'input-medium'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'input-medium'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'input-medium'}))


class SearchTempForm(forms.Form):
    ssn = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'SSN', 'class': 'input-medium'}))
    active = forms.ChoiceField(choices=(
        ('active', 'Active Only'),
        ('all', 'All Records'),
    ))


class SearchRepForm(forms.Form):
    rep = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Agencies'), empty_label='All Reps')


class SearchBranchForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='All Branches')


class SearchInterestCodeForm(forms.Form):
    interest_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Skill Keywords', 'class': 'input-medium'}))


class InterestCodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InterestCodeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.form_class = 'form-horizontal'

    class Meta:
        model = InterestCode
        fields = ('name', 'code', 'parent')


class InterestCodeSynonymFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InterestCodeSynonymFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-sm-2'
        self.field_class = 'col-sm-4'
        self.form_class = 'form-horizontal'

        base_layout = Layout(
            Field('name'),
            Div(

                Column(
                    Field('DELETE', ),
                    css_class='col-sm-offset-2 col-sm-8'
                ),
                css_class='form-group',
            )
        )

        self.add_layout(base_layout)


InterestCodeSynonymFormset = inlineformset_factory(
    InterestCode,
    InterestCodeSynonym,
    fields=('name',),
    can_delete=True
)



# ----------------- Customer Forms ----------------------


# Customer Search Filter Form
class CustomerSearchFilterForm(forms.Form):
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-large'}))
    customer_id = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
    active = forms.ChoiceField(choices=(
        ('active', 'Active Only'),
        ('all', 'All'),
    ))
    include_dept = forms.BooleanField(required=False, initial=False, label='Include Departments')
    accountmanager = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Agencies'), empty_label='All Sales Managers')
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='All Branches')


# Customer New Form
class CustomerNewForm(forms.ModelForm):
    customername = forms.CharField(required=True, max_length=100, label='Customer', widget=forms.TextInput(attrs={'class': 'form-control'}))
    customerdept = forms.CharField(label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'value': 'Primary', 'readonly': 'readonly'}))
    attnto = forms.CharField(required=False, max_length=100, label='Attn. To', widget=forms.TextInput(attrs={'class': 'form-control'}))

    note = forms.CharField(required=False, max_length=150, widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ('customername', 'customerdept',  'attnto', 'accountmanager', 'branch', 'note')

    def __init__(self, *args, **kwargs):
        super(CustomerNewForm, self).__init__(*args, **kwargs)

        self.fields['accountmanager'].label = 'Account Manager'

# Customer Details Form
class CustomerUpdateForm(forms.ModelForm):
    customername = forms.CharField(required=True, max_length=100, label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    customerdept = forms.CharField(label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'value': 'Primary', 'readonly': 'readonly'}))
    activedate = forms.CharField(required=False, label='Activation Date', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}) )
    createddate = forms.CharField(label='Date Created', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}) )

    attnto = forms.CharField(required=False, max_length=100, label='Attn. To', widget=forms.TextInput(attrs={'class': 'form-control'}))

    note = forms.CharField(required=False, max_length=150, widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

    interest_codes = TreeNodeMultipleChoiceField(required=False, queryset=InterestCode.objects.all())

    class Meta:
        model = Customer
        fields = ('id', 'customername', 'customerdept', 'status', 'activedate', 'createddate', 'website', 'attnto', 'billing_address_line_1', 'billing_address_line_2', 'billing_city', 'billing_state', 'billing_zip', 'billing_country', 'accountmanager', 'branch', 'note', 'interest_codes')

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['accountmanager'].label = 'Account Manager'
        self.fields['attnto'].label = 'Attention To'
        self.fields['billing_address_line_1'].label = 'Street 1'
        self.fields['billing_address_line_2'].label = 'Street 2'
        self.fields['billing_city'].label = 'City'
        self.fields['billing_state'].label = 'State'
        self.fields['billing_zip'].label = 'Zip'
        self.fields['billing_country'].label = 'Country'

        self.fields['interest_codes'].widget.attrs['class'] = 'chosen-select'
        self.fields['interest_codes'].widget.attrs['style'] = 'width:350px'


# Customer Billing Information Form
class CustomerBillingInformationForm(forms.ModelForm):

    invoice_notes = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}))

    class Meta:
        model = CustomerBillingInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerBillingInformationForm, self).__init__(*args, **kwargs)

        self.fields['bill_frequency'].label = 'Billing Frequency'
        self.fields['bill_on'].label = 'Bill On...'

        self.fields['invoice_style'].label = 'Style'
        self.fields['invoice_count'].label = 'Count'
        self.fields['invoice_method'].label = 'Invoice Method'
        self.fields['invoice_emailtemplate'].label = 'Email Template'
        self.fields['invoice_currency'].label = 'Currency'
        self.fields['invoice_handling'].label = 'Invoice Handling'
        self.fields['invoice_max'].label = 'Max Invoice'
        self.fields['invoice_notes'].label = 'Invoice Notes'

        self.fields['separate_department'].label = 'Department'
        self.fields['separate_branch'].label = 'Branch'
        self.fields['separate_order'].label = 'Order'
        self.fields['separate_worksite'].label = 'Worksite'
        self.fields['separate_assignment'].label = 'Assignment'
        self.fields['separate_supervisor'].label = 'Supervisor'
        self.fields['separate_employeeid'].label = 'Employee Id'
        self.fields['separate_jobtitle'].label = 'Job Title'
        self.fields['separate_weekend'].label = 'Week End'
        self.fields['separate_subentity'].label = 'Sub-entity'
        self.fields['separate_costcenter'].label = 'Cost Center'
        self.fields['separate_division'].label = 'Division'
        self.fields['separate_po'].label = 'PO'
        self.fields['separate_departmentaddress'].label = 'Department Address'


# Customer Credit Payroll Information Form
class CustomerCreditPayrollInformationForm(forms.ModelForm):

    class Meta:
        model = CustomerCreditPayrollInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerCreditPayrollInformationForm, self).__init__(*args, **kwargs)

        self.fields['credit_limit'].label = 'Credit Limit'
        self.fields['credit_analyst'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(groups__name='Agencies'))
        self.fields['credit_analyst'].label = 'Credit Analyst'
        self.fields['hold_code'].label = 'Hold Code'
        self.fields['terms'].label = 'Terms'
        self.fields['last_checked'].label = 'Last Checked'
        self.fields['customer_type'].label = 'Customer Type'
        self.fields['credit_note'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}))
        self.fields['credit_note'].label = 'Credit Note'

        self.fields['worker_comp'].label = 'Worker Comp'
        self.fields['check_delivery'].label = 'Check Delivery'
        self.fields['overtime_plan'].label = 'Overtime Plan'
        self.fields['pay_periods'].label = 'Pay Periods'
        self.fields['weekendson'].label = 'Week Ends On'
        self.fields['pay_cycle'].label = 'Pay Cycle'
        self.fields['mileage_rate'].label = 'Mileage Rate'
        self.fields['payroll_note'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}))
        self.fields['payroll_note'].label = 'Payroll Note'

        self.fields['ar_balance'].label = 'AR Balance'
        self.fields['ar_balance'].widget.attrs['readonly'] = True
        self.fields['ar_current'].label = 'AR Current'
        self.fields['ar_current'].widget.attrs['readonly'] = True
        self.fields['ar_1_30_days'].label = 'AR 1-30 Days'
        self.fields['ar_1_30_days'].widget.attrs['readonly'] = True
        self.fields['ar_31_60_days'].label = 'AR 31-60 Days'
        self.fields['ar_31_60_days'].widget.attrs['readonly'] = True
        self.fields['ar_61_90_days'].label = 'AR 61-90 Days'
        self.fields['ar_61_90_days'].widget.attrs['readonly'] = True
        self.fields['ar_over90_days'].label = 'AR Over 90 Days'
        self.fields['ar_over90_days'].widget.attrs['readonly'] = True
        self.fields['dso'].label = 'DSO'
        self.fields['dso'].widget.attrs['readonly'] = True
        self.fields['sales_tyd'].label = 'Sales TYD'
        self.fields['sales_tyd'].widget.attrs['readonly'] = True
        self.fields['sales_last12mo'].label = 'Sales Last 12 mo'
        self.fields['sales_last12mo'].widget.attrs['readonly'] = True
        self.fields['lifetime_sales'].label = 'Lifetime Sales'
        self.fields['lifetime_sales'].widget.attrs['readonly'] = True
        self.fields['volume_discount'].label = 'Volume Discount'
        self.fields['volume_discount'].widget.attrs['readonly'] = True


# Customer Misc Information Form
class CustomerMiscInformationForm(forms.ModelForm):

    class Meta:
        model = CustomerMiscInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerMiscInformationForm, self).__init__(*args, **kwargs)

        self.fields['edi_rpt'].label = 'EDI Rpt Number/Sort'
        self.fields['sic_code'].label = 'SIC Code'
        self.fields['alternate_customerid'].label = 'Alternate Cuustomer ID'
        self.fields['desired_gm'].label = 'Desired GM %'
        self.fields['alternate_branch_name'].label = 'Alternate Branch Name'
        self.fields['default_permanent_order'].label = 'Default Permanent Order %'
        self.fields['federal_employerid'].label = 'Federal Employer ID'
        self.fields['third_shift_starts_sunday'].label = '3rd Shift Starts Sunday'
        self.fields['auto_factor_invoices'].label = 'Auto Factor Invoices'

        self.fields['credit_number'].label = 'Card Number'
        self.fields['card_type'].label = 'Card Type'
        self.fields['card_expiration'].label = 'Card Expiration'
        self.fields['name_on_card'].label = 'Name on Card'


# ----------------- Order Forms ----------------------

# Order Search Filter Form
class OrderSearchFilterFormForAgency(forms.Form):
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-large'}))
    order_id = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
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

# Order New Form
class OrderNewFormForAgency(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(OrderNewFormForAgency, self).__init__(*args, **kwargs)
        if user:
            self.fields['customerdepartment'] = forms.ModelChoiceField(required=True, queryset=CustomerDepartment.objects.filter(parentdep__isnull=True))
            self.fields['customerdepartment'].required = True
            self.fields['customerdepartment'].label = 'Customer'
            self.fields['interest_codes'].required = False

# Customer Details Form
class OrderUpdateFormForAgency(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(OrderUpdateFormForAgency, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:            
            self.fields['customerdepartment'] = forms.ModelChoiceField(required=True, queryset=CustomerDepartment.objects.filter(customer__user__id=instance.customerdepartment.customer.user.id))
            self.fields['customerdepartment'].label = 'Department'
            self.fields['directions'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))

            self.fields['pay_rate'].label = 'Pay Rate'
            self.fields['bill_rate'].label = 'Bill Rate'
            self.fields['ot_pay'].label = 'Overtime Pay'
            self.fields['overtime_bill'].label = 'Overtime Bill'
            self.fields['dt_pay'].label = 'Doubletime Pay'
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

            self.fields['interest_codes'] = TreeNodeMultipleChoiceField(required=False, queryset=InterestCode.objects.all())
            self.fields['interest_codes'].widget.attrs['class'] = 'chosen-select'
            self.fields['interest_codes'].widget.attrs['style'] = 'width:350px'

            self.fields['start_date'].widget.attrs['class'] = 'date-picker'
            self.fields['start_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'

            self.fields['end_date'].widget.attrs['class'] = 'date-picker'
            self.fields['end_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'


# ----------------- Assignment Forms ----------------------

# Assignment New Form
class AssignmentNewFormForAgency(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        order = kwargs.pop('order')
        super(AssignmentNewFormForAgency, self).__init__(*args, **kwargs)


# Assignment Update Form
class AssignmentUpdateFormForAgency(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(AssignmentUpdateFormForAgency, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['customer_nda'].label = 'Customer NDA'
            self.fields['employee_nda'].label = 'Employee NDA'
            self.fields['ot_factor'].label = 'Overtime Factor'
            self.fields['bill_rate'].label = 'Bill Rate'
            self.fields['pay_rate'].label = 'Pay Rate'
            self.fields['expected_start_date'].label = 'Start Date'
            self.fields['expected_end_date'].label = 'Expected End Date'
            self.fields['original_start_date'].label = 'Original Start Date'
            self.fields['original_end_date'].label = 'Actual Date Ended'
            self.fields['workday_sunday'].label = 'Sunday'
            self.fields['workday_monday'].label = 'Monday'
            self.fields['workday_tuesday'].label = 'Tuesday'
            self.fields['workday_wednesday'].label = 'Wednesday'
            self.fields['workday_thursday'].label = 'Thursday'
            self.fields['workday_friday'].label = 'Friday'
            self.fields['workday_saturday'].label = 'Saturday'

            self.fields['shift_notes'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
            self.fields['payroll_notes'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
            self.fields['perf_notes'] = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))

            self.fields['status'].required = True
            self.fields['bill_rate'].required = True
            self.fields['pay_rate'].required = True
            self.fields['job_title'].required = True

            self.fields['rep'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(groups__name='Agencies'))
            self.fields['entered_by'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(groups__name='Agencies'))
            self.fields['referred_by'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(groups__name='Agencies'))

            self.fields['expected_start_date'].widget.attrs['class'] = 'date-picker'
            self.fields['expected_start_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
            self.fields['expected_end_date'].widget.attrs['class'] = 'date-picker'
            self.fields['expected_end_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
            self.fields['original_start_date'].widget.attrs['class'] = 'date-picker'
            self.fields['original_start_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
            self.fields['original_end_date'].widget.attrs['class'] = 'date-picker'
            self.fields['original_end_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'


# ------------ Time Entry Forms ----------------

# Time Entry Search Filter Form
class TimeEntrySearchFilterFormForAgency(forms.Form):
    status = forms.ModelChoiceField(queryset=TimeEntryStatus.objects.filter(), empty_label='All Statuses')
    order = forms.ModelChoiceField(queryset=WorkOrder.objects.filter(), empty_label='All Orders')        

    today = datetime.date.today()
    idx = today.weekday()
    sun = today + datetime.timedelta(6-idx)
    sundays = []
    sundays.append(['---','All Weekends'])
    while sun.year==today.year:
        sundays.append([sun,sun])
        sun = sun - datetime.timedelta(7)

    weekends = forms.ChoiceField(choices=sundays)

# Time Entry Update Form
class TimeEntryUpdateFormForAgency(forms.ModelForm):

    class Meta:
        model = TimeEntry
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TimeEntryUpdateFormForAgency, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['pay_roll'] = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))


# ------------ Incomplete Transactions Forms ----------------

# Incomplete Transaction Search Filter Form
class IncompleteTransactionSearchFilterFormForAgency(forms.Form):
    order = forms.ModelChoiceField(queryset=WorkOrder.objects.filter(), empty_label='All Orders')

    today = datetime.date.today()
    idx = today.weekday()
    sun = today + datetime.timedelta(6-idx)
    sundays = []
    sundays.append(['---','All Weekends'])
    while sun.year==today.year:
        sundays.append([sun,sun])
        sun = sun - datetime.timedelta(7)

    weekends = forms.ChoiceField(choices=sundays)


# -------------- Check Forms ------------------

# Check Search Filter Form
class CheckSearchFilterFormForAgency(forms.Form):

    employee_first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
    employee_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))


    today = datetime.date.today()
    idx = today.weekday()
    sun = today + datetime.timedelta(6-idx)
    sundays = []
    sundays.append(['---','All'])
    while sun.year==today.year:
        sundays.append([sun,sun])
        sun = sun - datetime.timedelta(7)

    weekends = forms.ChoiceField(choices=sundays)


# -------------- Invoice Forms ------------------

# Invoice Search Filter Form
class InvoiceSearchFilterFormForAgency(forms.Form):

    employee_first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
    employee_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '', 'class': 'input-medium'}))


    today = datetime.date.today()
    idx = today.weekday()
    sun = today + datetime.timedelta(6-idx)
    sundays = []
    sundays.append(['---','All'])
    while sun.year==today.year:
        sundays.append([sun,sun])
        sun = sun - datetime.timedelta(7)

    weekends = forms.ChoiceField(choices=sundays)