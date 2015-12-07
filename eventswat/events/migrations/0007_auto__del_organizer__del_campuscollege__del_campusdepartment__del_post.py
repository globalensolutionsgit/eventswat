# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Organizer'
        db.delete_table(u'events_organizer')

        # Deleting model 'CampusCollege'
        db.delete_table(u'events_campuscollege')

        # Deleting model 'CampusDepartment'
        db.delete_table(u'events_campusdepartment')

        # Removing M2M table for field college on 'CampusDepartment'
        db.delete_table(db.shorten_name(u'events_campusdepartment_college'))

        # Deleting model 'Postevent'
        db.delete_table(u'events_postevent')


    def backwards(self, orm):
        # Adding model 'Organizer'
        db.create_table(u'events_organizer', (
            ('organizer_email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('organizer_mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Postevent'])),
            ('organizer_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Organizer'])

        # Adding model 'CampusCollege'
        db.create_table(u'events_campuscollege', (
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('college_name', self.gf('django.db.models.fields.CharField')(max_length=150, unique=True)),
        ))
        db.send_create_signal(u'events', ['CampusCollege'])

        # Adding model 'CampusDepartment'
        db.create_table(u'events_campusdepartment', (
            ('department', self.gf('django.db.models.fields.CharField')(max_length=150, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'events', ['CampusDepartment'])

        # Adding M2M table for field college on 'CampusDepartment'
        m2m_table_name = db.shorten_name(u'events_campusdepartment_college')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campusdepartment', models.ForeignKey(orm[u'events.campusdepartment'], null=False)),
            ('campuscollege', models.ForeignKey(orm[u'events.campuscollege'], null=False))
        ))
        db.create_unique(m2m_table_name, ['campusdepartment_id', 'campuscollege_id'])

        # Adding model 'Postevent'
        db.create_table(u'events_postevent', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsCategory'])),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('enddate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('eventdescription', self.gf('django.db.models.fields.TextField')()),
            ('startdate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('eventtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsSubCategory'], null=True, blank=True)),
            ('payment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('admin_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('status_isactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['Postevent'])


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
        u'events.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'events.subcategoryrelatedfield': {
            'Meta': {'object_name': 'SubcategoryRelatedField'},
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.EventsSubCategory']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['events']