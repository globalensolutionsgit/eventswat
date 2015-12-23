# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PayuDetails'
        db.create_table(u'payu_payudetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mihpayid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('txnid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('productinfo', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('hash_key', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('error_Message', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bank_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pg_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('band_ref_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'payu', ['PayuDetails'])


    def backwards(self, orm):
        # Deleting model 'PayuDetails'
        db.delete_table(u'payu_payudetails')


    models = {
        u'payu.payudetails': {
            'Meta': {'object_name': 'PayuDetails'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'band_ref_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bank_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'error_Message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hash_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mihpayid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pg_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'productinfo': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'txnid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['payu']