# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'employers_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.City'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.State'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Country'])),
            ('weeks', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('days', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'employers', ['Job'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'employers_job')


    models = {
        u'agencies.staffingagency': {
            'Meta': {'object_name': 'StaffingAgency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'employers.job': {
            'Meta': {'object_name': 'Job'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'days': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.State']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weeks': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
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

    complete_apps = ['employers']