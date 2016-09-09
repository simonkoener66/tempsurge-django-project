# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StaffingAgency'
        db.create_table(u'agencies_staffingagency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'agencies', ['StaffingAgency'])

        # Adding model 'CompanyType'
        db.create_table(u'agencies_companytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['CompanyType'])

        # Adding model 'Company'
        db.create_table(u'agencies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('company_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fed_employer_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('company_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.CompanyType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pseudo_aident', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('street_1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('street_2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.City'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.State'])),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Country'])),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('local_address_1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('local_address_2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('local_address_city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='local_address_city', null=True, to=orm['geo.City'])),
            ('local_address_state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='local_address_state', null=True, to=orm['geo.State'])),
            ('local_address_zip', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('local_address_country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='local_address_country', null=True, to=orm['geo.Country'])),
            ('remittance_address_1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('remittance_address_2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('remittance_address_city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='remittance_address_city', null=True, to=orm['geo.City'])),
            ('remittance_address_state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='remittance_address_state', null=True, to=orm['geo.State'])),
            ('remittance_address_zip', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('remittance_address_country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='remittance_address_country', null=True, to=orm['geo.Country'])),
            ('small_business', self.gf('django.db.models.fields.BooleanField')()),
            ('minority_owned', self.gf('django.db.models.fields.BooleanField')()),
            ('women_owned', self.gf('django.db.models.fields.BooleanField')()),
            ('supplies_disabled_people', self.gf('django.db.models.fields.BooleanField')()),
            ('generate_1099', self.gf('django.db.models.fields.BooleanField')()),
            ('payment_terms', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['Company'])

        # Adding model 'BankAccount'
        db.create_table(u'agencies_bankaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('bank_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['BankAccount'])

        # Adding model 'Branch'
        db.create_table(u'agencies_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('branch_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('branch_full_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('branch_parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['agencies.Branch'])),
            ('branch_letter', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('branch_address', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('invoicing_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('branch_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.State'])),
            ('tax_state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tax_state', to=orm['geo.State'])),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Country'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.BankAccount'])),
            ('ap_bank', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ap_bank', to=orm['agencies.BankAccount'])),
            ('instant_bank', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instant_bank', to=orm['agencies.BankAccount'])),
            ('contractor_bank', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contractor_bank', to=orm['agencies.BankAccount'])),
            ('ar_rank', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ar_rank', to=orm['agencies.BankAccount'])),
            ('calc_sales_tax_by_gross_profit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('instant_pay_limit', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Company'])),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'agencies', ['Branch'])

        # Adding model 'Authority'
        db.create_table(u'agencies_authority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['Authority'])

        # Adding model 'AdjustmentCategory'
        db.create_table(u'agencies_adjustmentcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['AdjustmentCategory'])

        # Adding model 'Adjustment'
        db.create_table(u'agencies_adjustment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.AdjustmentCategory'])),
            ('txn_relative', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.StaffingAgency'])),
        ))
        db.send_create_signal(u'agencies', ['Adjustment'])

        # Adding model 'TimeEntry'
        db.create_table(u'agencies_timeentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('billrate', self.gf('django.db.models.fields.FloatField')()),
            ('otbill', self.gf('django.db.models.fields.FloatField')()),
            ('dtbill', self.gf('django.db.models.fields.FloatField')()),
            ('payrate', self.gf('django.db.models.fields.FloatField')()),
            ('otpay', self.gf('django.db.models.fields.FloatField')()),
            ('dtpay', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'agencies', ['TimeEntry'])


    def backwards(self, orm):
        # Deleting model 'StaffingAgency'
        db.delete_table(u'agencies_staffingagency')

        # Deleting model 'CompanyType'
        db.delete_table(u'agencies_companytype')

        # Deleting model 'Company'
        db.delete_table(u'agencies_company')

        # Deleting model 'BankAccount'
        db.delete_table(u'agencies_bankaccount')

        # Deleting model 'Branch'
        db.delete_table(u'agencies_branch')

        # Deleting model 'Authority'
        db.delete_table(u'agencies_authority')

        # Deleting model 'AdjustmentCategory'
        db.delete_table(u'agencies_adjustmentcategory')

        # Deleting model 'Adjustment'
        db.delete_table(u'agencies_adjustment')

        # Deleting model 'TimeEntry'
        db.delete_table(u'agencies_timeentry')


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
        u'agencies.timeentry': {
            'Meta': {'object_name': 'TimeEntry'},
            'billrate': ('django.db.models.fields.FloatField', [], {}),
            'dtbill': ('django.db.models.fields.FloatField', [], {}),
            'dtpay': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otbill': ('django.db.models.fields.FloatField', [], {}),
            'otpay': ('django.db.models.fields.FloatField', [], {}),
            'payrate': ('django.db.models.fields.FloatField', [], {})
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
        }
    }

    complete_apps = ['agencies']