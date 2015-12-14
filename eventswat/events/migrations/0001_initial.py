# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'events_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'events', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'events_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('hover_icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'events', ['SubCategory'])

        # Adding M2M table for field category on 'SubCategory'
        m2m_table_name = db.shorten_name(u'events_subcategory_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subcategory', models.ForeignKey(orm[u'events.subcategory'], null=False)),
            ('category', models.ForeignKey(orm[u'events.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subcategory_id', 'category_id'])

        # Adding model 'City'
        db.create_table(u'events_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('state', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('country_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'events', ['City'])

        # Adding model 'College'
        db.create_table(u'events_college', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'])),
            ('college_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'events', ['College'])

        # Adding model 'Department'
        db.create_table(u'events_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal(u'events', ['Department'])

        # Adding model 'CollegeDepartment'
        db.create_table(u'events_collegedepartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Department'], null=True)),
        ))
        db.send_create_signal(u'events', ['CollegeDepartment'])

        # Adding M2M table for field college on 'CollegeDepartment'
        m2m_table_name = db.shorten_name(u'events_collegedepartment_college')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('collegedepartment', models.ForeignKey(orm[u'events.collegedepartment'], null=False)),
            ('college', models.ForeignKey(orm[u'events.college'], null=False))
        ))
        db.create_unique(m2m_table_name, ['collegedepartment_id', 'college_id'])

        # Adding model 'Postevent'
        db.create_table(u'events_postevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('startdate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('enddate', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Category'])),
            ('eventtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.SubCategory'], null=True, blank=True)),
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
        db.send_create_signal(u'events', ['Postevent'])

        # Adding model 'Organizer'
        db.create_table(u'events_organizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Postevent'])),
            ('organizer_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organizer_mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organizer_email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Organizer'])

        # Adding model 'Feedback'
        db.create_table(u'events_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'events', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'events_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'events_subcategory')

        # Removing M2M table for field category on 'SubCategory'
        db.delete_table(db.shorten_name(u'events_subcategory_category'))

        # Deleting model 'City'
        db.delete_table(u'events_city')

        # Deleting model 'College'
        db.delete_table(u'events_college')

        # Deleting model 'Department'
        db.delete_table(u'events_department')

        # Deleting model 'CollegeDepartment'
        db.delete_table(u'events_collegedepartment')

        # Removing M2M table for field college on 'CollegeDepartment'
        db.delete_table(db.shorten_name(u'events_collegedepartment_college'))

        # Deleting model 'Postevent'
        db.delete_table(u'events_postevent')

        # Deleting model 'Organizer'
        db.delete_table(u'events_organizer')

        # Deleting model 'Feedback'
        db.delete_table(u'events_feedback')


    models = {
        u'events.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'enddate': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eventdescription': ('django.db.models.fields.TextField', [], {}),
            'eventtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.SubCategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status_isactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'events.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['events.Category']", 'symmetrical': 'False'}),
            'hover_icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['events']