# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CampusCollege'
        db.create_table(u'postevent_campuscollege', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collegetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsCategory'], null=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'])),
            ('college_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'postevent', ['CampusCollege'])

        # Adding model 'CampusDepartment'
        db.create_table(u'postevent_campusdepartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'postevent', ['CampusDepartment'])

        # Adding M2M table for field college on 'CampusDepartment'
        m2m_table_name = db.shorten_name(u'postevent_campusdepartment_college')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campusdepartment', models.ForeignKey(orm[u'postevent.campusdepartment'], null=False)),
            ('campuscollege', models.ForeignKey(orm[u'postevent.campuscollege'], null=False))
        ))
        db.create_unique(m2m_table_name, ['campusdepartment_id', 'campuscollege_id'])

        # Adding model 'Postevent'
        db.create_table(u'postevent_postevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('startdate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('enddate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsCategory'])),
            ('eventtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventsSubCategory'], null=True, blank=True)),
            ('eventdescription', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True)),
            ('admin_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('payment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status_isactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'postevent', ['Postevent'])

        # Adding model 'Organizer'
        db.create_table(u'postevent_organizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postevent.Postevent'])),
            ('organizer_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organizer_mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organizer_email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
        ))
        db.send_create_signal(u'postevent', ['Organizer'])


    def backwards(self, orm):
        # Deleting model 'CampusCollege'
        db.delete_table(u'postevent_campuscollege')

        # Deleting model 'CampusDepartment'
        db.delete_table(u'postevent_campusdepartment')

        # Removing M2M table for field college on 'CampusDepartment'
        db.delete_table(db.shorten_name(u'postevent_campusdepartment_college'))

        # Deleting model 'Postevent'
        db.delete_table(u'postevent_postevent')

        # Deleting model 'Organizer'
        db.delete_table(u'postevent_organizer')


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
            'collegetype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventsCategory']", 'null': 'True'}),
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