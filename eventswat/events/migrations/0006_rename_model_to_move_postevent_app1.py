# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('postevent_campusdepartment_college', 'collegedepartment_id', 'campusdepartment_id')
        db.rename_column('postevent_campusdepartment_college', 'college_id', 'campuscollege_id')
        db.rename_table('events_postevent', 'postevent_postevent') 
        db.rename_table('events_organizer', 'postevent_organizer')

    def backwards(self, orm):
        db.rename_column('postevent_campusdepartment_college', 'campusdepartment_id', 'collegedepartment_id')
        db.rename_column('postevent_campusdepartment_college', 'campuscollege_id', 'college_id')
        db.rename_table('postevent_postevent', 'events_postevent') 
        db.rename_table('postevent_organizer', 'events_organizer')

    models = {
        u'events.campuscollege': {
            'Meta': {'object_name': 'CampusCollege'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.City']"}),
            'college_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.campusdepartment': {
            'Meta': {'object_name': 'CampusDepartment'},
            'college': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.CampusCollege']", 'symmetrical': 'False'}),
            'department': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'events.eventscategory': {
            'Meta': {'object_name': 'EventsCategory'},
            'category_hover_icon': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'category_icon': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'category_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.eventssubcategory': {
            'Meta': {'object_name': 'EventsSubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategory_hover_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subcategory_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subcategory_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        },
        u'events.subcategoryrelatedfield': {
            'Meta': {'object_name': 'SubcategoryRelatedField'},
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsSubCategory']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['events']