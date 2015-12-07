# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CampusCollege.collegetype'
        db.delete_column(u'postevent_campuscollege', 'collegetype_id')


    def backwards(self, orm):
        # Adding field 'CampusCollege.collegetype'
        db.add_column(u'postevent_campuscollege', 'collegetype',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsCategory'], null=True),
                      keep_default=False)


    models = {
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
        u'postevent.campuscollege': {
            'Meta': {'object_name': 'CampusCollege'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.City']"}),
            'college_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'postevent.campusdepartment': {
            'Meta': {'object_name': 'CampusDepartment'},
            'college': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['postevent.CampusCollege']", 'symmetrical': 'False'}),
            'department': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'postevent.organizer': {
            'Meta': {'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizer_email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'organizer_mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organizer_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postevent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['postevent.Postevent']"})
        },
        u'postevent.postevent': {
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

    complete_apps = ['postevent']