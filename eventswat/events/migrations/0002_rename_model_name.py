# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('events_category', 'events_eventscategory') 
        db.rename_table('events_subcategory', 'events_eventssubcategory')
        db.rename_table('events_subcategory_category', 'events_eventssubcategory_category')

    def backwards(self, orm):
        db.rename_table('events_eventscategory', 'events_category')     
        db.rename_table('events_eventssubcategory', 'events_subcategory')
        db.rename_table('events_eventssubcategory_category', 'events_subcategory_category')

    models = {
        u'events.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'events.college': {
            'Meta': {'object_name': 'College'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.City']"}),
            'college_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.collegedepartment': {
            'Meta': {'object_name': 'CollegeDepartment'},
            'college': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.College']", 'null': 'True', 'symmetrical': 'False'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Department']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.department': {
            'Meta': {'object_name': 'Department'},
            'department': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.eventscategory': {
            'Meta': {'object_name': 'EventsCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'events.eventssubcategory': {
            'Meta': {'object_name': 'EventsSubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsCategory']", 'symmetrical': 'False'}),
            'hover_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'events.organizer': {
            'Meta': {'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizer_email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'organizer_mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organizer_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postevent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Postevent']"})
        },
        u'events.postevent': {
            'Meta': {'object_name': 'Postevent'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'admin_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventsCategory']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'enddate': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eventdescription': ('django.db.models.fields.TextField', [], {}),
            'eventtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventsSubCategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status_isactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['events']