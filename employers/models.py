from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from temps.models import Temp, InterestCode

# Create your models here.



# -------------- Customer Model ---------------

class CustomerStatus(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name + "(" + self.description + ")"

class Customer(models.Model):
	customername = models.CharField(max_length=100)
	attnto = models.CharField(max_length=75, blank=True)
	accountmanager = models.ForeignKey('auth.User', related_name='accountmanager', blank=True, null=True)
	branch = models.ForeignKey('agencies.Branch', related_name='branch', blank=True, null=True)
	note = models.CharField(max_length=150, blank=True)
	user = models.OneToOneField('auth.User')
	createddate = models.DateTimeField(auto_now_add=True, auto_now=False)
	createddate.editable = True
	activedate = models.DateTimeField(blank=True, null=True)
	status = models.ForeignKey('employers.CustomerStatus', related_name='customerstatus', blank=True, null=True)
	website = models.CharField(max_length=150, blank=True, null=True, default='')

	billing_address_line_1 = models.CharField(max_length=250, blank=True)
	billing_address_line_2 = models.CharField(max_length=250, blank=True)
	billing_city = models.ForeignKey('geo.City', blank=True, null=True)
	billing_state = models.ForeignKey('geo.State', blank=True, null=True)
	billing_zip = models.CharField(max_length=10, blank=True)
	billing_country = models.ForeignKey('geo.Country', blank=True, null=True)

	interest_codes = models.ManyToManyField(InterestCode)

	def __unicode__(self):
		return self.customername

class CustomerDepartment(models.Model):
	customer = models.ForeignKey('employers.Customer', related_name='customer', blank=False, null=False)
	depname = models.CharField(max_length=100)
	parentdep = models.ForeignKey('employers.CustomerDepartment', related_name='parentdepartment', blank=True, null=True)
	active = models.BooleanField(default=True)
	activedate = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.customer.customername + " / " + self.depname

# -------------- Customer Billing Information Model ---------------

class BillFrequency(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class BillOn(models.Model):
	cycle = models.CharField(max_length=10)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.description

class InvoiceStyle(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class InvoiceMethod(models.Model):
	method = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.method

class InvoiceEmailTemplate(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name

class CurrencyType(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class InvoiceHandling(models.Model):
	code = models.IntegerField()
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.description

class CustomerBillingInformation(models.Model):
	bill_frequency = models.ForeignKey('employers.BillFrequency', related_name='billing_frequency', blank=True, null=True)
	bill_on = models.ForeignKey('employers.BillOn', related_name='bill_on', blank=True, null=True)

	invoice_style = models.ForeignKey('employers.InvoiceStyle', related_name='invoice_style', blank=True, null=True)
	invoice_count = models.IntegerField(default=1)
	invoice_method = models.ForeignKey('employers.InvoiceMethod', related_name='invoice_method', blank=True, null=True)
	invoice_emailtemplate = models.ForeignKey('employers.InvoiceEmailTemplate', related_name='invoice_emailtemplate', blank=True, null=True)
	invoice_currency = models.ForeignKey('employers.CurrencyType', related_name='invoice_currency', blank=True, null=True)
	invoice_handling = models.ForeignKey('employers.InvoiceHandling', related_name='invoice_handling', blank=True, null=True)
	invoice_max = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)

	separate_department = models.BooleanField(default=False)
	separate_branch = models.BooleanField(default=False)
	separate_order = models.BooleanField(default=False)
	separate_worksite = models.BooleanField(default=False)
	separate_assignment = models.BooleanField(default=False)
	separate_supervisor = models.BooleanField(default=False)
	separate_employeeid = models.BooleanField(default=False)
	separate_jobtitle = models.BooleanField(default=False)
	separate_weekend = models.BooleanField(default=False)
	separate_subentity = models.BooleanField(default=False)
	separate_costcenter = models.BooleanField(default=False)
	separate_division = models.BooleanField(default=False)
	separate_po = models.BooleanField(default=False)
	separate_departmentaddress = models.BooleanField(default=False)

	invoice_notes = models.CharField(max_length=500, blank=True, null=True)

	user = models.OneToOneField('auth.User')

# -------------- Customer Credit Payroll Information Model ---------------

class CreditHoldCode(models.Model):
	code = models.CharField(max_length=20)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.code + '  '  + self.description

class CreditTerms(models.Model):
	terms = models.CharField(max_length=100)

	def __unicode__(self):
		return self.terms

class CustomerType(models.Model):
	customertype = models.CharField(max_length=20)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.customertype

class WorkerComp(models.Model):
	code = models.CharField(max_length=50)
	percentage = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	description = models.CharField(max_length=300)
	state = models.ForeignKey('geo.State', blank=True, null=True)

class PayrollCheckDelivery(models.Model):
	code = models.CharField(max_length=50)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.code + " -- " + self.description

class PayrollOvertimePlan(models.Model):
	plan = models.CharField(max_length=50)
	plantype = models.CharField(max_length=50)

	def __unicode__(self):
		return self.plan + " -- " + self.plantype

class CustomerCreditPayrollInformation(models.Model):
	credit_limit = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	credit_analyst = models.ForeignKey('auth.User', related_name='credit_analyst', blank=True, null=True)

	hold_code = models.ForeignKey('employers.CreditHoldCode', related_name='holdcode', blank=True, null=True)
	terms = models.ForeignKey('employers.CreditTerms', related_name='creditterms', blank=True, null=True)
	last_checked = models.DateField(blank=True, null=True)

	customer_type = models.ForeignKey('employers.CustomerType', related_name='creditcustomertype', blank=True, null=True)
	credit_note = models.CharField(max_length=500, blank=True, null=True)

	worker_comp = models.ForeignKey('employers.WorkerComp', related_name='worker_comp', blank=True, null=True)
	check_delivery = models.ForeignKey('employers.PayrollCheckDelivery', related_name='check_delivery', blank=True, null=True)
	overtime_plan = models.ForeignKey('employers.PayrollOvertimePlan', related_name='overtime_plan', blank=True, null=True)
	pay_periods = models.IntegerField(default = 0)
	weekendson = models.CharField(max_length=20, blank=True, null=True, choices=(
		('Sunday', 'Sunday'),
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
	))
	pay_cycle = models.IntegerField(default=1)
	mileage_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	payroll_note = models.CharField(max_length=1000, blank=True, null=True)

	ar_balance = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ar_current = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ar_1_30_days = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ar_31_60_days = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ar_61_90_days = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ar_over90_days = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	dso = models.IntegerField(blank=True, null=True, default=0)
	sales_tyd = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	sales_last12mo = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	lifetime_sales = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	volume_discount = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)

	user = models.OneToOneField('auth.User')


# -------------- Customer Misc Information Model ---------------

class SICCode(models.Model):
	code = models.CharField(max_length=50)
	description = models.CharField(max_length=300, blank=True, null=True)

	def __unicode__(self):
		return self.code

class CreditCardType(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class CustomerMiscInformation(models.Model):
	edi_rpt = models.CharField(max_length=500, blank=True, null=True)
	sic_code = models.ForeignKey('employers.SICCode', related_name='sic_code', blank=True, null=True)
	alternate_customerid = models.IntegerField(blank=True, null=True)
	desired_gm = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
	alternate_branch_name = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	default_permanent_order = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	federal_employerid = models.IntegerField(blank=True, null=True)
	third_shift_starts_sunday  = models.BooleanField(default=False)
	auto_factor_invoices = models.BooleanField(default=False)

	credit_number = models.CharField(max_length=100, blank=True, null=True)
	card_type = models.ForeignKey('employers.CreditCardType', related_name='credit_cardtype', blank=True, null=True)
	card_expiration = models.DateField(blank=True, null=True)
	name_on_card = models.CharField(max_length=100, blank=True, null=True)

	user = models.OneToOneField('auth.User')


# -------------- Order Model ---------------

class WorkOrderType(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False)
	shortname = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return self.name

class JobTitle(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False)	

	def __unicode__(self):
		return self.name

class WorkOrder(models.Model):

	customerdepartment = models.ForeignKey('employers.CustomerDepartment', related_name='customerdepartment', blank=True, null=True)
	#customer work site
	#customer work comp
	#pulling in from customer work site
	directions = models.CharField(max_length=500, blank=True, null=True)

	capacity_required = models.IntegerField(blank=True, null=True, default=1)
	capacity_assigned = models.IntegerField(blank=True, null=True, default=0)
	order_type = models.ForeignKey('employers.WorkOrderType', related_name='ordertype', blank=True, null=True)
	job_title = models.ForeignKey('employers.JobTitle', related_name='jobtitle', blank=True, null=True)
	description = models.CharField(max_length=500, blank=True, null=True)
	#pulling in from customer work site
	dress_code = models.CharField(max_length=100, blank=True, null=True)
	safety_notes = models.CharField(max_length=500, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	duration = models.CharField(max_length=20, blank=True, null=True, choices=(
        ('Indef', 'Indef'),        
    ))
	end_date = models.DateField(blank=True, null=True)
	shift = models.CharField(max_length=20, blank=True, null=True, choices=(
    	('Early Morning', 'Early Morning'),
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),        
    ))
	start_time = models.TimeField(blank=True, null=True)
	end_time = models.TimeField(blank=True, null=True)
	shift_notes = models.CharField(max_length=500, blank=True, null=True)
	workday_sunday = models.BooleanField(default=False)
	workday_monday = models.BooleanField(default=True)
	workday_tuesday = models.BooleanField(default=True)
	workday_wednesday = models.BooleanField(default=True)
	workday_thursday = models.BooleanField(default=True)
	workday_friday = models.BooleanField(default=True)
	workday_saturday = models.BooleanField(default=False)

	pay_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	ot_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	dt_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	bill_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	overtime_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	doubletime_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	overtime_plan = models.CharField(max_length=20, blank=True, null=True, choices=(
        ('PlanSTD', 'PlanSTD'),        
    ), default='PlanSTD')
	ot_factor = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	multiplier = models.CharField(max_length=20, blank=True, null=True, choices=(
        ('None', 'None'),
        ('1.21 Markup', '1.21 Markup')
    ), default='None')
	pay_periods = models.IntegerField(blank=True, null=True)
	gp_percent = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	gp_estimate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	desired_gm = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	
	#contacts

	active = models.BooleanField(default=True)
	status = models.CharField(max_length=20, blank=True, null=True, choices=(
        ('Unfilled', 'Unfilled'),
        ('Filled', 'Filled'),
        ('Closed', 'Closed'),
    ), default='Unfilled')
	rep = models.ForeignKey(User, related_name='representative', blank=True, null=True)
	branch = models.ForeignKey('agencies.Branch', related_name='sales_branch', blank=True, null=True)
	#taken by
	#sales team
	do_not_auto_close = models.BooleanField(default = False)
	notes = models.CharField(max_length=500, blank=True, null=True)

	officephone = models.CharField(max_length=50, blank=True)

	interest_codes = models.ManyToManyField(InterestCode)

	def __unicode__(self):
		return str(self.id) + ": " + self.customerdepartment.customer.customername + " / " + self.customerdepartment.depname + " / " + self.job_title.name


# -------------- Assignment Model ---------------

class BusinessCode(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False)	

	def __unicode__(self):
		return self.name

class Assignment(models.Model):

	order = models.ForeignKey('employers.WorkOrder', related_name='assignment_workorder', blank=True, null=True)
	employee = models.ForeignKey(Temp, related_name='assignment_employee', blank=True, null=True)

	temp_phone = models.CharField(max_length=50, blank=True)
	status = models.CharField(max_length=20, blank=True, null=True, choices=(
		('Open', 'Open'),
		('Closed', 'Closed'),		
	), default='Open')
	replaces = models.ForeignKey('employers.Assignment', related_name='assignment_replaces', blank=True, null=True)
	customer_nda = models.BooleanField(default = False)
	employee_nda = models.BooleanField(default = False)

	job_title = models.ForeignKey('employers.JobTitle', related_name='assignment_jobtitle', blank=True, null=True)
	business_code = models.ForeignKey('employers.BusinessCode', related_name='assignment_businesscode', blank=True, null=True)
	expected_start_date = models.DateField(blank=True, null=True)
	expected_end_date = models.DateField(blank=True, null=True)
	original_start_date = models.DateField(blank=True, null=True)
	original_end_date = models.DateField(blank=True, null=True)
	shift = models.CharField(max_length=20, blank=True, null=True, choices=(
		('Early Morning', 'Early Morning'),
		('Morning', 'Morning'),
		('Afternoon', 'Afternoon'),
		('Evening', 'Evening'),        
	))
	start_time = models.TimeField(blank=True, null=True)
	end_time = models.TimeField(blank=True, null=True)
	shift_notes = models.CharField(max_length=500, blank=True, null=True)
	workday_sunday = models.BooleanField(default=False)
	workday_monday = models.BooleanField(default=True)
	workday_tuesday = models.BooleanField(default=True)
	workday_wednesday = models.BooleanField(default=True)
	workday_thursday = models.BooleanField(default=True)
	workday_friday = models.BooleanField(default=True)
	workday_saturday = models.BooleanField(default=False)

	multiplier = models.CharField(max_length=20, blank=True, null=True, choices=(
		('None', 'None'),
		('1.21 Markup', '1.21 Markup')
	), default='None')
	ot_factor = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	pay_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	bill_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	salary = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	salary_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	units_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	units_pay_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	other_agency_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	overtime_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	overtime_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	doubletime_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	doubletime_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, default=0)
	payroll_notes = models.CharField(max_length=500, blank=True, null=True)

	rep = models.ForeignKey(User, related_name='assignment_representative', blank=True, null=True)
	entered_by = models.ForeignKey(User, related_name='assignment_enteredby', blank=True, null=True)
	referred_by = models.ForeignKey(User, related_name='assignment_referredby', blank=True, null=True)
	branch = models.ForeignKey('agencies.Branch', related_name='assignment_sales_branch', blank=True, null=True)
	do_not_auto_close = models.BooleanField(default = False)
	assigned_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	perf_notes = models.CharField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return '#' + str(self.id) + ": " + self.order.customerdepartment.customer.customername + "/" + self.order.customerdepartment.depname + "/" + self.order.job_title.name + "---" + self.employee.user.first_name + " " +self.employee.user.last_name