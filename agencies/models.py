from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from employers.models import WorkOrder, Assignment
from temps.models import Temp



# -------------------- Agency Model --------------------

class StaffingAgency(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Staffing Agencies'


# -------------------- Company Models --------------------

class CompanyType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    active = models.BooleanField(default=True)
    company_id = models.CharField(max_length=30)
    fed_employer_id = models.CharField(max_length=25)
    company_type = models.ForeignKey(CompanyType)
    name = models.CharField(max_length=50)
    pseudo_aident = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    street_1 = models.CharField(max_length=250, blank=True)
    street_2 = models.CharField(max_length=250, blank=True)
    city = models.ForeignKey('geo.City')
    state = models.ForeignKey('geo.State')
    zip = models.CharField(max_length=15, blank=True)
    country = models.ForeignKey('geo.Country')
    contact_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=True)
    local_address_1 = models.CharField(max_length=250, blank=True)
    local_address_2 = models.CharField(max_length=250, blank=True)
    local_address_city = models.ForeignKey('geo.City', related_name='local_address_city', blank=True, null=True)
    local_address_state = models.ForeignKey('geo.State', related_name='local_address_state', blank=True, null=True)
    local_address_zip = models.CharField(max_length=15, blank=True)
    local_address_country = models.ForeignKey('geo.Country', related_name='local_address_country', blank=True, null=True)
    remittance_address_1 = models.CharField(max_length=250, blank=True)
    remittance_address_2 = models.CharField(max_length=250, blank=True)
    remittance_address_city = models.ForeignKey('geo.City', related_name='remittance_address_city', blank=True, null=True)
    remittance_address_state = models.ForeignKey('geo.State', related_name='remittance_address_state', blank=True, null=True)
    remittance_address_zip = models.CharField(max_length=15, blank=True)
    remittance_address_country = models.ForeignKey('geo.Country', related_name='remittance_address_country', blank=True, null=True)
    small_business = models.BooleanField()
    minority_owned = models.BooleanField()
    women_owned = models.BooleanField()
    supplies_disabled_people = models.BooleanField()
    generate_1099 = models.BooleanField()
    payment_terms = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


# -------------------- Bank Account Model --------------------

class BankAccount(models.Model):
    active = models.BooleanField(default=True)
    bank_name = models.CharField(max_length=50)
    # More fields to be added here...
    agency = models.ForeignKey(StaffingAgency)


# -------------------- Branch Model --------------------

class Branch(MPTTModel):
    # Main branch Info
    active = models.BooleanField(default=True)
    branch_name = models.CharField(max_length=50)
    branch_full_name = models.CharField(max_length=50)
    branch_parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    branch_letter = models.CharField(max_length=5)
    branch_address = models.CharField(max_length=250, blank=True)
    invoicing_address = models.TextField(blank=True)
    branch_state = models.ForeignKey('geo.State')
    tax_state = models.ForeignKey('geo.State', related_name='tax_state')
    # hier = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    country = models.ForeignKey('geo.Country')
    phone = models.CharField(max_length=250, blank=True)
    fax = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=True)
    # auto_invoice_day =
    # Identifications
    # EINC =
    bank = models.ForeignKey(BankAccount)
    ap_bank = models.ForeignKey(BankAccount, related_name='ap_bank')
    instant_bank = models.ForeignKey(BankAccount, related_name='instant_bank')
    contractor_bank = models.ForeignKey(BankAccount, related_name='contractor_bank')
    ar_rank = models.ForeignKey(BankAccount, related_name='ar_rank')
    # Worker comp options
    # default_worker_comp = ...
    calc_sales_tax_by_gross_profit = models.BooleanField(default=False)
    # Payroll options
    instant_pay_limit = models.DecimalField(max_digits=7, decimal_places=2)
    # Technical
    # branch_scanner_ip_address = ...
    # branch_scanner_type = ...
    # doccenter packages = ...
    company = models.ForeignKey(Company)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return "Company: %s / Branch: %s" % (self.company.name, self.branch_name)

    class Meta:
        verbose_name_plural = 'Branches'

    class MPTTMeta:
        parent_attr = 'branch_parent'
        order_insertion_by = ['branch_name']


# -------------------- Authorities --------------------

class Authority(models.Model):
    name = models.CharField(max_length=100)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authorities'


# -------------------- Adjustments --------------------

class AdjustmentCategory(models.Model):
    name = models.CharField(max_length=100)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Adjustment Categories'


class Adjustment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(AdjustmentCategory)
    txn_relative = models.BooleanField(default=False)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

class PayCode(models.Model):
    shortname = models.CharField(max_length=30)
    fullname = models.CharField(max_length=100)

    def __unicode__(self):
        return self.shortname


# -------------------- Time Entry Model --------------------

class TimeEntryStatus(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class TimeEntry(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='timeentry_assignment', blank=False, null=False)

    we_bill = models.DateField(blank=True, null=True)
    we_date = models.DateField(blank=True, null=True)
    work_date = models.DateField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    pay_code = models.ForeignKey(PayCode, related_name='timeentry_paycode', blank=True, null=True)
    pay_roll = models.CharField(max_length=500, blank=True)

    hours_regular = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_overtime = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_doubletime = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    hours_day1 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day2 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day3 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day4 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day5 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day6 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_day7 = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    salary = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    bill_amount = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    hours_total_regular = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    salary_approved = models.BooleanField()

    units = models.IntegerField(blank=True, null=True)
    units_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    units_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    bill_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    ot_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    dt_bill = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    pay_rate = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    ot_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    dt_pay = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    adj_gross = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    adj_net = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    ot_plan = models.CharField(max_length=100, blank=True, null=True)
         
    status = models.ForeignKey(TimeEntryStatus, related_name='timeentry_status', blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Time Entries'

    def __unicode__(self):
        return str(self.assignment.order.id) + ": " + self.assignment.order.customerdepartment.depname + " / " + self.assignment.order.job_title.name + ' - ' + self.we_bill.strftime('%m/%d/%Y');


# -------------------- Check Model --------------------

class Check(models.Model):

    timeentry = models.ForeignKey(TimeEntry, related_name='check_timeentry', blank=False, null=False)

    checkdate = models.DateField(blank=True, null=True)

    gross = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    tax = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    net = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

# -------------------- Invoice Model --------------------
    
class Invoice(models.Model):

    timeentry = models.ForeignKey(TimeEntry, related_name='invoice_timeentry', blank=False, null=False)

    invoicedate = models.DateField(blank=True, null=True)

    gross = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    tax = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    net = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)