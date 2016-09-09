from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# -------------------- Interest Code Models --------------------

class InterestCode(MPTTModel):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=7)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    agency = models.ForeignKey('agencies.StaffingAgency')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class InterestCodeSynonym(models.Model):
    name = models.CharField(max_length=250, verbose_name='Synonym')
    interest_code = models.ForeignKey(InterestCode)

    def __unicode__(self):
        return self.name


# -------------------- Transportation Model --------------------

class TransportationType(models.Model):
    name = models.CharField(max_length=50)
    agency = models.ForeignKey('agencies.StaffingAgency')

    def __unicode__(self):
        return self.name


# -------------------- Temp Prodfile Model --------------------

class Temp(models.Model):
    OrderType = models.CharField(max_length=2, blank=True)
    SMS = models.TextField(blank=True)
    rep = models.ForeignKey('auth.User', related_name='rep', blank=True, null=True)
    entered_by_rep = models.ForeignKey('auth.User', related_name='entered_by_rep')
    InterviewedByRepName = models.ForeignKey('auth.User', related_name='Interviewed_By_Rep_Name', blank=True, null=True)
    EmploymentCategory = models.TextField(blank=True)
    AIdent = models.TextField(blank=True)
    ssn = models.CharField(max_length=9, blank=True)
    active = models.BooleanField(default=True)
    assigned = models.BooleanField(default=False)
    WashedStatus = models.BooleanField(default=False)
    Burden = models.TextField(blank=True)
    ActivationDate = models.DateTimeField(blank=True)
    DeActivationDate = models.DateTimeField(blank=True, null=True)
    YTDEarnings = models.IntegerField(blank=True, null=True)
    OtherAddress = models.TextField(blank=True)
    SecurityClearance = models.TextField(blank=True)
    DrugTest = models.TextField(blank=True)
    MaritalTaxStatusId = models.PositiveSmallIntegerField(blank=True, null=True)
    Birthday = models.CharField(max_length=10, blank=True)
    state_exemptions = models.PositiveSmallIntegerField(blank=True, null=True)
    federal_exemptions = models.PositiveSmallIntegerField(blank=True, null=True)
    Dependents = models.PositiveSmallIntegerField(blank=True, null=True)
    MailCheck = models.BooleanField(default=True)
    EmergencyContact = models.TextField(blank=True)
    RightToWork = models.BooleanField(default=False)
    _18orOlder = models.BooleanField(default=False)
    Smoker = models.BooleanField(default=False)
    ResumeOnfile = models.BooleanField(default=False)
    CarAvailable = models.BooleanField(default=False)
    TransportationDetails = models.TextField(blank=True)
    I9Submitted = models.BooleanField(default=False)
    Education = models.TextField(blank=True)
    DrugTested = models.BooleanField(default=False)
    BackgroundChecked = models.BooleanField(default=False)
    Convictions = models.TextField(blank=True)
    ECurrentAssignment = models.TextField(blank=True)
    EExpEnd = models.TextField(blank=True)
    EPayRate = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    ELastPerf = models.CharField(max_length=10, blank=True, null=True)
    EPayrollNote = models.TextField(blank=True)
    TicklerDate = models.DateTimeField(blank=True, null=True)
    Class = models.CharField(max_length=10)
    last_message = models.TextField(blank=True)
    LastDate = models.DateTimeField(blank=True, null=True)
    WComp = models.TextField(blank=True)
    CheckPayDay = models.CharField(max_length=10, blank=True)
    LocalTaxCode = models.TextField(blank=True)
    TaxModel = models.TextField(blank=True)
    TaxInitialized = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    CheckDelivery = models.TextField(blank=True)
    ElectronicPay = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    PayPeriods = models.SmallIntegerField(blank=True, null=True)
    LastModified = models.DateTimeField(blank=True, null=True)
    LastModifiedBySrident = models.SmallIntegerField(blank=True, null=True)
    OrientationGiven = models.DateTimeField(blank=True, null=True)
    EndDateAssign = models.DateTimeField(blank=True, null=True)
    StartDateAssign = models.DateTimeField(blank=True, null=True)
    ESort = models.IntegerField(default=0, blank=True, null=True)
    AnniversaryDate = models.DateTimeField(blank=True, null=True)
    EStatus = models.CharField(max_length=10, blank=True)
    ENote = models.TextField(blank=True)
    ReferencesChecked = models.BooleanField(default=False)
    DrugAlcPolicy = models.TextField(blank=True)
    HarassmentPolicy = models.BooleanField(default=False)
    DMVCheck = models.BooleanField(default=False)
    ReferencesClear = models.BooleanField(default=False)
    AlienRegistration = models.TextField(blank=True)
    AdditionalWH = models.TextField(blank=True)
    TaxExempt = models.TextField(blank=True)
    EMiscDate1 = models.DateTimeField(blank=True, null=True)
    InterviewedBySrident = models.SmallIntegerField(blank=True, null=True)
    DateRefCheck = models.DateTimeField(blank=True, null=True)
    DateBCheck = models.DateTimeField(blank=True, null=True)
    DateDTest = models.DateTimeField(blank=True, null=True)
    I9Date = models.DateTimeField(blank=True, null=True)
    DLState = models.TextField(blank=True)
    DLNumber = models.TextField(blank=True)
    DLClass = models.TextField(blank=True)
    SafetyCert = models.TextField(blank=True)
    DLExpire = models.DateTimeField(blank=True, null=True)
    CountyJuris = models.TextField(blank=True)
    CityJuris = models.TextField(blank=True)
    SchoolJuris = models.TextField(blank=True)
    LocalJuris = models.TextField(blank=True)
    PrAlert = models.TextField(blank=True)
    AltBranchName = models.TextField(blank=True)
    AltENum = models.TextField(blank=True)
    ChangeMailToTo = models.TextField(blank=True)
    TaxState = models.ForeignKey('geo.State', related_name='TaxState', blank=True, null=True)
    LastBBPHazcomDate = models.DateTimeField(blank=True, null=True)
    StateJuris = models.TextField(blank=True, null=True)
    LastTaxModification = models.DateTimeField(blank=True, null=True)
    pin = models.PositiveSmallIntegerField(blank=True, null=True)
    ChangeDeliveryDate = models.DateTimeField(blank=True, null=True)
    ChangeDeliveryTo = models.DateTimeField(blank=True, null=True)
    addphone = models.CharField(max_length=1, blank=True)
    EnteredBySrident = models.PositiveSmallIntegerField(blank=True, null=True)
    Country = models.ForeignKey('geo.Country', blank=True, null=True)
    LocCode = models.TextField(blank=True)
    TempMailingAddress = models.TextField(blank=True)
    TempMailingCity = models.TextField(blank=True)
    TempMailingZip = models.TextField(blank=True)
    TempMailingState = models.TextField(blank=True)
    TempMailingCountry = models.TextField(blank=True)
    TempAddressActive = models.TextField(blank=True)
    SchoolDistrictCode = models.TextField(blank=True)
    CityCode = models.TextField(blank=True)
    CountyCode = models.TextField(blank=True)
    HowHeardOfDetail = models.TextField(blank=True)
    SchoolTaxExempt = models.TextField(blank=True)
    CityTaxExempt = models.TextField(blank=True)
    CountyTaxExempt = models.TextField(blank=True)
    SID = models.TextField(blank=True)
    AStatus = models.TextField(blank=True)
    DepartmentName = models.TextField(blank=True)
    CustomerId = models.TextField(blank=True)
    CompanyName = models.TextField(blank=True)
    ajobtitle = models.TextField(blank=True)
    hierid = models.TextField(blank=True)
    CompanyIdent = models.TextField(blank=True)
    LastAvl = models.TextField(blank=True)
    Rating = models.PositiveSmallIntegerField(blank=True, null=True)
    PayReady = models.BooleanField(default=False)
    RecordOriginId = models.IntegerField(blank=True, null=True)
    DateCreated = models.DateTimeField()
    W4Date = models.DateTimeField(blank=True, null=True)
    ResumeDate = models.DateTimeField(blank=True, null=True)
    WarningFlags = models.TextField(blank=True)
    DefaultPayRate = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    einc = models.PositiveSmallIntegerField(verbose_name="EINC", blank=True, null=True)
    HierIdCC = models.PositiveSmallIntegerField(blank=True, null=True)
    HierCC = models.PositiveSmallIntegerField(blank=True, null=True)
    CPPExempt = models.BooleanField(default=False)
    IsHouseAident = models.BooleanField(default=False)
    DefaultCustomerIdForAsg = models.TextField(blank=True)
    EIExempt = models.BooleanField(default=False)
    EEORecordExists = models.BooleanField(default=False)
    BypassTr = models.BooleanField(default=False)
    UnemploymentClaimDate = models.DateTimeField(blank=True, null=True)
    ActiveStatus = models.BooleanField(default=True)
    AssignedStatus = models.BooleanField(default=True)
    EmployeeRootGuid = models.CharField(max_length=36)
    DefaultPayDiff = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    SSNVerified = models.BooleanField(default=False)
    PayMethodID = models.PositiveSmallIntegerField(blank=True, null=True)
    PayDeliveryMethodID = models.PositiveSmallIntegerField(blank=True, null=True)
    ContactId = models.IntegerField(blank=True, null=True)
    employmentCategoryID = models.CharField(max_length=36)
    HowHeardOfId = models.IntegerField(blank=True, null=True)
    OTPlanId = models.IntegerField(blank=True, null=True)
    OrderTypeId = models.IntegerField(blank=True, null=True)
    TransportationTypeGUID = models.CharField(max_length=36, blank=True)
    TaxByEmployeeState = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    ConsentToReleaseConvictions = models.IntegerField(blank=True, null=True)
    CountryCode = models.IntegerField(blank=True, null=True)
    SrIdent = models.IntegerField(blank=True, null=True)
    ZipFive = models.IntegerField(blank=True, null=True)
    has_resume = models.BooleanField(default=False)
    # --- Transportation
    transportation_available = models.BooleanField(default=False)
    transportation_type = models.ForeignKey(TransportationType, blank=True, null=True)
    transportation_details = models.TextField(blank=True)
    license_state = models.ForeignKey('geo.State', related_name='license_state', blank=True, null=True)
    license_number = models.CharField(max_length=20, blank=True)
    license_class = models.BooleanField(default=False)
    dmv_check = models.BooleanField(verbose_name='DMV Check', default=False)
    license_expire = models.DateField(blank=True, null=True)
    # --- Electronic Payment
    activate_electronic_payments = models.BooleanField(default=False)
    electronic_payment_method = models.CharField(max_length=7, blank=True, choices=(
        ('ach', 'ACH Bank Account'),
        ('paycard', 'PayCard Account')
    ))
    branch = models.ManyToManyField('agencies.Branch')
    interest_codes = models.ManyToManyField(InterestCode)
    user = models.OneToOneField('auth.User')

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name


# -------------------- Assignment Restriction Model --------------------

class AssignmentRestriction(models.Model):
    description = models.TextField(blank=True)
    all_departments = models.BooleanField(default=False)
    customer_dna_employee = models.BooleanField(verbose_name='CustomerDNAEmployee', default=False)
    employee_dna_customer = models.BooleanField(verbose_name='EmployeeDNACustomer', default=False)
    branch = models.ForeignKey('agencies.Branch', verbose_name='Client')
    temp = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.description


# -------------------- Pay Setup Models --------------------

class ACHBankAccount(models.Model):
    bank_routing_info = models.CharField(max_length=20, blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    account_type = models.CharField(max_length=1, blank=True, choices=(
        ('c', 'Checking'),
        ('s', 'Saving')
    ))
    pre_note_sent = models.DateField(verbose_name='Pre-note Sent', blank=True, null=True)
    pre_note_approved = models.DateField(verbose_name='Pre-note Approved', blank=True, null=True)
    pre_note_disapproved = models.DateField(verbose_name='Pre-note Disapproved', blank=True, null=True)
    user = models.OneToOneField('auth.User')


class PayCardAccount(models.Model):
    account_number = models.CharField(max_length=20, blank=True)
    expiry_date = models.DateField(blank=True, null=True)
    paycard_verified_by = models.CharField(max_length=20, blank=True)
    paycard_verify_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField('auth.User')


# -------------------- Adjustment Model --------------------

class Adjustment(models.Model):
    description = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=True)
    frequency = models.CharField(max_length=2, choices=(
        ('w', 'Weekly'),
        ('bw', 'Bi-Weekly'),
        ('sm', 'Semi-Monthly'),
        ('m', 'Monthly'),
        ('d', 'Daily'),
    ))
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    deduct_greater_or_lesser = models.CharField(max_length=1, choices=(
        ('g', 'Deduct Greater'),
        ('l', 'Deduct Lesser')
    ), default='l', help_text='The lesser or greater amount to be deducted.')
    sequence = models.IntegerField(blank=True, null=True)
    date_served = models.DateField(blank=True, null=True)
    max_monthly = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    max_yearly = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    max_lifetime = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    period_max = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    max_after_calc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    authority = models.ForeignKey('agencies.Authority', blank=True, null=True)
    case_number = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=250, blank=True)
    adjustment = models.ForeignKey('agencies.Adjustment')
    user = models.ForeignKey('auth.User')


class AdjustmentRule(models.Model):
    deduction_amount = models.DecimalField(verbose_name='Amount', max_digits=7, decimal_places=2, default=0.00)
    deduction_amount_type = models.CharField(verbose_name='Amount Type', max_length=1, choices=(
        ('d', 'Dollars'),
        ('p', 'Percent of')
    ), default='d')
    deduction_amount_from_total = models.CharField(verbose_name='Deduct from total', max_length=1, blank=True, choices=(
        ('g', 'Gross Pay'),
        ('n', 'Net Pay'),
        ('h', 'Hourly Rate')
    ))
    apply_if_can_deducted = models.BooleanField(verbose_name='Only apply this rule if all of the adjustment can be deducted', default=False)
    set_maximum_deduction = models.BooleanField(default=False)
    maximum_deduction_amount = models.DecimalField(verbose_name='Amount', max_digits=7, decimal_places=2, blank=True, null=True)
    maximum_deduction_amount_type = models.CharField(verbose_name='Amount Type', max_length=1, blank=True, choices=(
        ('d', 'Dollars'),
        ('p', 'Percent of')
    ))
    maximum_deduction_from_total = models.CharField(verbose_name='Deduct from total', max_length=1, blank=True, choices=(
        ('g', 'Gross Pay'),
        ('n', 'Net Pay'),
        ('h', 'Hourly Rate')
    ))
    when_to_apply = models.CharField(verbose_name='When to apply this rule', max_length=1, choices=(
        ('a', 'Always apply this rule'),
        ('c', 'Only when a condition is met')
    ), default='a')
    when_to_apply_pay_type = models.CharField(verbose_name='Pay Type', max_length=1, blank=True, choices=(
        ('g', 'Gross Pay'),
        ('n', 'Net Pay'),
        ('h', 'Hourly Rate')
    ))
    when_to_apply_operator = models.CharField(verbose_name='Operator', max_length=2, blank=True, choices=(
        ('<=', '<='),
        ('=', '='),
        ('>', '>'),
        ('<', '<'),
        ('>=', '>=')
    ))
    when_to_apply_amount = models.DecimalField(verbose_name='Amount', max_digits=7, decimal_places=2, blank=True, null=True)
    adjustment = models.ForeignKey('temps.Adjustment')