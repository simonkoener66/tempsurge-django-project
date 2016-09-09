# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TimeEntry.webill'
        db.add_column(u'agencies_timeentry', 'webill',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TimeEntry.wedate'
        db.add_column(u'agencies_timeentry', 'wedate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TimeEntry.workdate'
        db.add_column(u'agencies_timeentry', 'workdate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TimeEntry.invdate'
        db.add_column(u'agencies_timeentry', 'invdate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TimeEntry.webill'
        db.delete_column(u'agencies_timeentry', 'webill')

        # Deleting field 'TimeEntry.wedate'
        db.delete_column(u'agencies_timeentry', 'wedate')

        # Deleting field 'TimeEntry.workdate'
        db.delete_column(u'agencies_timeentry', 'workdate')

        # Deleting field 'TimeEntry.invdate'
        db.delete_column(u'agencies_timeentry', 'invdate')


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
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employer'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'otbill': ('django.db.models.fields.FloatField', [], {}),
            'otpay': ('django.db.models.fields.FloatField', [], {}),
            'payrate': ('django.db.models.fields.FloatField', [], {}),
            'webill': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'wedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'workdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['agencies']