# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):


        # Adding unique constraint on 'City', fields ['city', 'state', 'country_code', 'country_name']
        db.create_unique(u'events_city', ['city', 'state', 'country_code', 'country_name'])

        # Adding unique constraint on 'SubcategoryRelatedField', fields ['field_name']
        db.create_unique(u'events_subcategoryrelatedfield', ['field_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'SubcategoryRelatedField', fields ['field_name']
        db.delete_unique(u'events_subcategoryrelatedfield', ['field_name'])

        # Removing unique constraint on 'City', fields ['city', 'state', 'country_code', 'country_name']
        db.delete_unique(u'events_city', ['city', 'state', 'country_code', 'country_name'])


    models = {
        u'events.city': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('city', 'state', 'country_code', 'country_name'),)", 'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'events.eventscategory': {
            'Meta': {'ordering': "['id']", 'object_name': 'EventsCategory'},
            'category_hover_icon': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'category_icon': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'category_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.eventssubcategory': {
            'Meta': {'ordering': "['id']", 'object_name': 'EventsSubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategory_hover_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subcategory_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subcategory_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.subcategoryrelatedfield': {
            'Meta': {'ordering': "['id']", 'object_name': 'SubcategoryRelatedField'},
            'field_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsSubCategory']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['events']
