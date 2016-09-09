# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TransportationType'
        db.create_table(u'temps_transportationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'temps', ['TransportationType'])

        # Deleting field 'InterestCodeSynonym.interest_codes'
        db.delete_column(u'temps_interestcodesynonym', 'interest_code_id')

        # Adding field 'InterestCodeSynonym.interest_code'
        db.add_column(u'temps_interestcodesynonym', 'interest_code',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['temps.InterestCode']),
                      keep_default=False)

        # Adding field 'Temp.transportation_available'
        db.add_column(u'temps_temp', 'transportation_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Temp.transportation_type'
        db.add_column(u'temps_temp', 'transportation_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['temps.TransportationType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Temp.transportation_details'
        db.add_column(u'temps_temp', 'transportation_details',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Temp.license_state'
        db.add_column(u'temps_temp', 'license_state',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='license_state', null=True, to=orm['geo.State']),
                      keep_default=False)

        # Adding field 'Temp.license_number'
        db.add_column(u'temps_temp', 'license_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'Temp.license_class'
        db.add_column(u'temps_temp', 'license_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Temp.dmv_check'
        db.add_column(u'temps_temp', 'dmv_check',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Temp.license_expire'
        db.add_column(u'temps_temp', 'license_expire',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TransportationType'
        db.delete_table(u'temps_transportationtype')

        # Adding field 'InterestCodeSynonym.interest_codes'
        db.add_column(u'temps_interestcodesynonym', 'interest_codes',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['temps.InterestCode']),
                      keep_default=False)

        # Deleting field 'InterestCodeSynonym.interest_code'
        db.delete_column(u'temps_interestcodesynonym', 'interest_code_id')

        # Deleting field 'Temp.transportation_available'
        db.delete_column(u'temps_temp', 'transportation_available')

        # Deleting field 'Temp.transportation_type'
        db.delete_column(u'temps_temp', 'transportation_type_id')

        # Deleting field 'Temp.transportation_details'
        db.delete_column(u'temps_temp', 'transportation_details')

        # Deleting field 'Temp.license_state'
        db.delete_column(u'temps_temp', 'license_state_id')

        # Deleting field 'Temp.license_number'
        db.delete_column(u'temps_temp', 'license_number')

        # Deleting field 'Temp.license_class'
        db.delete_column(u'temps_temp', 'license_class')

        # Deleting field 'Temp.dmv_check'
        db.delete_column(u'temps_temp', 'dmv_check')

        # Deleting field 'Temp.license_expire'
        db.delete_column(u'temps_temp', 'license_expire')


    models = {
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
            'EINC': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addphone': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ajobtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'assigned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'branch': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['agencies.Branch']", 'symmetrical': 'False'}),
            'dmv_check': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employmentCategoryID': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'entered_by_rep': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entered_by_rep'", 'to': u"orm['auth.User']"}),
            'federal_exemptions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_resume': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hierid': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_codes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['temps.InterestCode']", 'symmetrical': 'False'}),
            'last_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'license_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'license_expire': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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