# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InterestCode'
        db.create_table(u'temps_interestcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['temps.InterestCode'])),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'temps', ['InterestCode'])

        # Adding model 'InterestCodeSynonym'
        db.create_table(u'temps_interestcodesynonym', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('interest_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['temps.InterestCode'])),
        ))
        db.send_create_signal(u'temps', ['InterestCodeSynonym'])

        # Adding model 'TransportationType'
        db.create_table(u'temps_transportationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'temps', ['TransportationType'])

        # Adding model 'Temp'
        db.create_table(u'temps_temp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('OrderType', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('SMS', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rep', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='rep', null=True, to=orm['auth.User'])),
            ('entered_by_rep', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entered_by_rep', to=orm['auth.User'])),
            ('InterviewedByRepName', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Interviewed_By_Rep_Name', null=True, to=orm['auth.User'])),
            ('EmploymentCategory', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('AIdent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('assigned', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('WashedStatus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Burden', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ActivationDate', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('DeActivationDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('YTDEarnings', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('OtherAddress', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SecurityClearance', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DrugTest', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('MaritalTaxStatusId', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('Birthday', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('state_exemptions', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('federal_exemptions', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('Dependents', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('MailCheck', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('EmergencyContact', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('RightToWork', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('_18orOlder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Smoker', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ResumeOnfile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('CarAvailable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('TransportationDetails', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('I9Submitted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Education', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DrugTested', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('BackgroundChecked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Convictions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ECurrentAssignment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('EExpEnd', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('EPayRate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('ELastPerf', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('EPayrollNote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TicklerDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Class', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('last_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('LastDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('WComp', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CheckPayDay', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('LocalTaxCode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TaxModel', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TaxInitialized', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('CheckDelivery', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ElectronicPay', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('PayPeriods', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('LastModified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('LastModifiedBySrident', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('OrientationGiven', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('EndDateAssign', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('StartDateAssign', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ESort', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('AnniversaryDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('EStatus', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('ENote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ReferencesChecked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('DrugAlcPolicy', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('HarassmentPolicy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('DMVCheck', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ReferencesClear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('AlienRegistration', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('AdditionalWH', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TaxExempt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('EMiscDate1', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('InterviewedBySrident', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('DateRefCheck', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('DateBCheck', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('DateDTest', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('I9Date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('DLState', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DLNumber', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DLClass', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SafetyCert', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DLExpire', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('CountyJuris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CityJuris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SchoolJuris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('LocalJuris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('PrAlert', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('AltBranchName', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('AltENum', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ChangeMailToTo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TaxState', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='TaxState', null=True, to=orm['geo.State'])),
            ('LastBBPHazcomDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('StateJuris', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('LastTaxModification', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('pin', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('ChangeDeliveryDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ChangeDeliveryTo', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('addphone', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('EnteredBySrident', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('Country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Country'], null=True, blank=True)),
            ('LocCode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempMailingAddress', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempMailingCity', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempMailingZip', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempMailingState', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempMailingCountry', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('TempAddressActive', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SchoolDistrictCode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CityCode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CountyCode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('HowHeardOfDetail', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SchoolTaxExempt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CityTaxExempt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CountyTaxExempt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('SID', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('AStatus', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DepartmentName', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CustomerId', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CompanyName', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ajobtitle', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hierid', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('CompanyIdent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('LastAvl', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('Rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('PayReady', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('RecordOriginId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('DateCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('W4Date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ResumeDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('WarningFlags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('DefaultPayRate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('einc', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('HierIdCC', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('HierCC', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('CPPExempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('IsHouseAident', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('DefaultCustomerIdForAsg', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('EIExempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('EEORecordExists', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('BypassTr', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('UnemploymentClaimDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ActiveStatus', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('AssignedStatus', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('EmployeeRootGuid', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('DefaultPayDiff', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('SSNVerified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('PayMethodID', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('PayDeliveryMethodID', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('ContactId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('employmentCategoryID', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('HowHeardOfId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('OTPlanId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('OrderTypeId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('TransportationTypeGUID', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('TaxByEmployeeState', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('ConsentToReleaseConvictions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CountryCode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('SrIdent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ZipFive', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('has_resume', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transportation_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transportation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['temps.TransportationType'], null=True, blank=True)),
            ('transportation_details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('license_state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='license_state', null=True, to=orm['geo.State'])),
            ('license_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('license_class', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dmv_check', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('license_expire', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('activate_electronic_payments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('electronic_payment_method', self.gf('django.db.models.fields.CharField')(max_length=7, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'temps', ['Temp'])

        # Adding M2M table for field branch on 'Temp'
        m2m_table_name = db.shorten_name(u'temps_temp_branch')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('temp', models.ForeignKey(orm[u'temps.temp'], null=False)),
            ('branch', models.ForeignKey(orm[u'agencies.branch'], null=False))
        ))
        db.create_unique(m2m_table_name, ['temp_id', 'branch_id'])

        # Adding M2M table for field interest_codes on 'Temp'
        m2m_table_name = db.shorten_name(u'temps_temp_interest_codes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('temp', models.ForeignKey(orm[u'temps.temp'], null=False)),
            ('interestcode', models.ForeignKey(orm[u'temps.interestcode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['temp_id', 'interestcode_id'])

        # Adding model 'AssignmentRestriction'
        db.create_table(u'temps_assignmentrestriction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('all_departments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('customer_dna_employee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('employee_dna_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Branch'])),
            ('temp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'temps', ['AssignmentRestriction'])

        # Adding model 'ACHBankAccount'
        db.create_table(u'temps_achbankaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank_routing_info', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('account_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('account_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('pre_note_sent', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('pre_note_approved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('pre_note_disapproved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'temps', ['ACHBankAccount'])

        # Adding model 'PayCardAccount'
        db.create_table(u'temps_paycardaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paycard_verified_by', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('paycard_verify_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'temps', ['PayCardAccount'])

        # Adding model 'Adjustment'
        db.create_table(u'temps_adjustment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('deduct_greater_or_lesser', self.gf('django.db.models.fields.CharField')(default='l', max_length=1)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_served', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('max_monthly', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('max_yearly', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('max_lifetime', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('period_max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('max_after_calc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('authority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Authority'], null=True, blank=True)),
            ('case_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('adjustment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Adjustment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'temps', ['Adjustment'])

        # Adding model 'AdjustmentRule'
        db.create_table(u'temps_adjustmentrule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deduction_amount', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2)),
            ('deduction_amount_type', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('deduction_amount_from_total', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('apply_if_can_deducted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('set_maximum_deduction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('maximum_deduction_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('maximum_deduction_amount_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('maximum_deduction_from_total', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('when_to_apply', self.gf('django.db.models.fields.CharField')(default='a', max_length=1)),
            ('when_to_apply_pay_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('when_to_apply_operator', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('when_to_apply_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('adjustment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['temps.Adjustment'])),
        ))
        db.send_create_signal(u'temps', ['AdjustmentRule'])


    def backwards(self, orm):
        # Deleting model 'InterestCode'
        db.delete_table(u'temps_interestcode')

        # Deleting model 'InterestCodeSynonym'
        db.delete_table(u'temps_interestcodesynonym')

        # Deleting model 'TransportationType'
        db.delete_table(u'temps_transportationtype')

        # Deleting model 'Temp'
        db.delete_table(u'temps_temp')

        # Removing M2M table for field branch on 'Temp'
        db.delete_table(db.shorten_name(u'temps_temp_branch'))

        # Removing M2M table for field interest_codes on 'Temp'
        db.delete_table(db.shorten_name(u'temps_temp_interest_codes'))

        # Deleting model 'AssignmentRestriction'
        db.delete_table(u'temps_assignmentrestriction')

        # Deleting model 'ACHBankAccount'
        db.delete_table(u'temps_achbankaccount')

        # Deleting model 'PayCardAccount'
        db.delete_table(u'temps_paycardaccount')

        # Deleting model 'Adjustment'
        db.delete_table(u'temps_adjustment')

        # Deleting model 'AdjustmentRule'
        db.delete_table(u'temps_adjustmentrule')


    models = {
        u'agencies.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.AdjustmentCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'txn_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'agencies.adjustmentcategory': {
            'Meta': {'object_name': 'AdjustmentCategory'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'agencies.authority': {
            'Meta': {'object_name': 'Authority'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'agencies.bankaccount': {
            'Meta': {'object_name': 'BankAccount'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencies.branch': {
            'Meta': {'object_name': 'Branch'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'ap_bank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ap_bank'", 'to': u"orm['agencies.BankAccount']"}),
            'ar_rank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ar_rank'", 'to': u"orm['agencies.BankAccount']"}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.BankAccount']"}),
            'branch_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'branch_full_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'branch_letter': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'branch_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'branch_parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['agencies.Branch']"}),
            'branch_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.State']"}),
            'calc_sales_tax_by_gross_profit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Company']"}),
            'contractor_bank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contractor_bank'", 'to': u"orm['agencies.BankAccount']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instant_bank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instant_bank'", 'to': u"orm['agencies.BankAccount']"}),
            'instant_pay_limit': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'invoicing_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tax_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tax_state'", 'to': u"orm['geo.State']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'agencies.company': {
            'Meta': {'object_name': 'Company'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']"}),
            'company_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'company_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.CompanyType']"}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fed_employer_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'generate_1099': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_address_1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'local_address_2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'local_address_city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'local_address_city'", 'null': 'True', 'to': u"orm['geo.City']"}),
            'local_address_country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'local_address_country'", 'null': 'True', 'to': u"orm['geo.Country']"}),
            'local_address_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'local_address_state'", 'null': 'True', 'to': u"orm['geo.State']"}),
            'local_address_zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'minority_owned': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'payment_terms': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pseudo_aident': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'remittance_address_1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'remittance_address_2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'remittance_address_city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'remittance_address_city'", 'null': 'True', 'to': u"orm['geo.City']"}),
            'remittance_address_country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'remittance_address_country'", 'null': 'True', 'to': u"orm['geo.Country']"}),
            'remittance_address_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'remittance_address_state'", 'null': 'True', 'to': u"orm['geo.State']"}),
            'remittance_address_zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'small_business': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.State']"}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'supplies_disabled_people': ('django.db.models.fields.BooleanField', [], {}),
            'women_owned': ('django.db.models.fields.BooleanField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'agencies.companytype': {
            'Meta': {'object_name': 'CompanyType'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'agencies.staffingagency': {
            'Meta': {'object_name': 'StaffingAgency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'geo.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'geo.country': {
            'Meta': {'ordering': "['order']", 'object_name': 'Country'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'alpha_2_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'alpha_3_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numeric_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True', 'max_length': '3'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '3'})
        },
        u'geo.state': {
            'Meta': {'ordering': "['name']", 'object_name': 'State'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'temps.achbankaccount': {
            'Meta': {'object_name': 'ACHBankAccount'},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'account_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'bank_routing_info': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_note_approved': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'pre_note_disapproved': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'pre_note_sent': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'temps.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adjustment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Adjustment']"}),
            'authority': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Authority']", 'null': 'True', 'blank': 'True'}),
            'case_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_served': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deduct_greater_or_lesser': ('django.db.models.fields.CharField', [], {'default': "'l'", 'max_length': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_after_calc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'max_lifetime': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'max_monthly': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'max_yearly': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'period_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'temps.adjustmentrule': {
            'Meta': {'object_name': 'AdjustmentRule'},
            'adjustment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['temps.Adjustment']"}),
            'apply_if_can_deducted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deduction_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'}),
            'deduction_amount_from_total': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'deduction_amount_type': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximum_deduction_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'maximum_deduction_amount_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'maximum_deduction_from_total': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'set_maximum_deduction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'when_to_apply': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '1'}),
            'when_to_apply_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'when_to_apply_operator': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'when_to_apply_pay_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'temps.assignmentrestriction': {
            'Meta': {'object_name': 'AssignmentRestriction'},
            'all_departments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Branch']"}),
            'customer_dna_employee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'employee_dna_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'temps.interestcode': {
            'Meta': {'object_name': 'InterestCode'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['temps.InterestCode']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'temps.interestcodesynonym': {
            'Meta': {'object_name': 'InterestCodeSynonym'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['temps.InterestCode']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'temps.paycardaccount': {
            'Meta': {'object_name': 'PayCardAccount'},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paycard_verified_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'paycard_verify_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'temps.temp': {
            'AIdent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'AStatus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ActivationDate': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'ActiveStatus': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'AdditionalWH': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'AlienRegistration': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'AltBranchName': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'AltENum': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'AnniversaryDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'AssignedStatus': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'BackgroundChecked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Birthday': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'Burden': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'BypassTr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CPPExempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CarAvailable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ChangeDeliveryDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ChangeDeliveryTo': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ChangeMailToTo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CheckDelivery': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CheckPayDay': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'CityCode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CityJuris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CityTaxExempt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'CompanyIdent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CompanyName': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ConsentToReleaseConvictions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ContactId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Convictions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']", 'null': 'True', 'blank': 'True'}),
            'CountryCode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CountyCode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CountyJuris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CountyTaxExempt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'CustomerId': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DLClass': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DLExpire': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'DLNumber': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DLState': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DMVCheck': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'DateBCheck': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'DateCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'DateDTest': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'DateRefCheck': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'DeActivationDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'DefaultCustomerIdForAsg': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DefaultPayDiff': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'DefaultPayRate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'DepartmentName': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Dependents': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'DrugAlcPolicy': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DrugTest': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'DrugTested': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ECurrentAssignment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'EEORecordExists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'EExpEnd': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'EIExempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ELastPerf': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'EMiscDate1': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ENote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'EPayRate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'EPayrollNote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ESort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'EStatus': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'Education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ElectronicPay': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'EmergencyContact': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'EmployeeRootGuid': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'EmploymentCategory': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'EndDateAssign': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'EnteredBySrident': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'HarassmentPolicy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'HierCC': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'HierIdCC': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'HowHeardOfDetail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'HowHeardOfId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'I9Date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'I9Submitted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'InterviewedByRepName': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Interviewed_By_Rep_Name'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'InterviewedBySrident': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'IsHouseAident': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'LastAvl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'LastBBPHazcomDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LastDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LastModified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LastModifiedBySrident': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'LastTaxModification': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'LocCode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'LocalJuris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'LocalTaxCode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'MailCheck': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'MaritalTaxStatusId': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Temp'},
            'OTPlanId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'OrderType': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'OrderTypeId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'OrientationGiven': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'OtherAddress': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'PayDeliveryMethodID': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'PayMethodID': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'PayPeriods': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'PayReady': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'PrAlert': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'RecordOriginId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ReferencesChecked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ReferencesClear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ResumeDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ResumeOnfile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'RightToWork': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'SID': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SMS': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SSNVerified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'SafetyCert': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SchoolDistrictCode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SchoolJuris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SchoolTaxExempt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'SecurityClearance': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Smoker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'SrIdent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'StartDateAssign': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'StateJuris': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'TaxByEmployeeState': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'TaxExempt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TaxInitialized': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'TaxModel': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TaxState': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'TaxState'", 'null': 'True', 'to': u"orm['geo.State']"}),
            'TempAddressActive': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TempMailingAddress': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TempMailingCity': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TempMailingCountry': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TempMailingState': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TempMailingZip': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TicklerDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'TransportationDetails': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'TransportationTypeGUID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'UnemploymentClaimDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'W4Date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'WComp': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'WarningFlags': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'WashedStatus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'YTDEarnings': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ZipFive': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_18orOlder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'activate_electronic_payments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addphone': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ajobtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'assigned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'branch': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['agencies.Branch']", 'symmetrical': 'False'}),
            'dmv_check': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'einc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electronic_payment_method': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'employmentCategoryID': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'entered_by_rep': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entered_by_rep'", 'to': u"orm['auth.User']"}),
            'federal_exemptions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_resume': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hierid': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_codes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['temps.InterestCode']", 'symmetrical': 'False'}),
            'last_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'license_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'license_expire': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'license_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'license_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'license_state'", 'null': 'True', 'to': u"orm['geo.State']"}),
            'pin': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rep': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'rep'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'state_exemptions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transportation_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transportation_details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'transportation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['temps.TransportationType']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'temps.transportationtype': {
            'Meta': {'object_name': 'TransportationType'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.StaffingAgency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['temps']