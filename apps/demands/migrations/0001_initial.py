# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Severity'
        db.create_table(u'demands_severity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'demands', ['Severity'])

        # Adding model 'Priority'
        db.create_table(u'demands_priority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'demands', ['Priority'])

        # Adding model 'Status'
        db.create_table(u'demands_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'demands', ['Status'])

        # Adding model 'Domain'
        db.create_table(u'demands_domain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'demands', ['Domain'])

        # Adding model 'SubDomain'
        db.create_table(u'demands_subdomain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'subdomains', to=orm['demands.Domain'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'demands', ['SubDomain'])

        # Adding model 'Ticket'
        db.create_table(u'demands_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'created_tickets', to=orm['auth.User'])),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demands.Domain'], null=True, blank=True)),
            ('subdomain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demands.SubDomain'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demands.Status'])),
            ('severity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demands.Severity'], null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demands.Priority'], null=True, blank=True)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_workload', self.gf('timedelta.fields.TimedeltaField')(null=True, blank=True)),
            ('is_linked_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'related_tickets', null=True, to=orm['demands.Ticket'])),
            ('parent_ticket', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'children', null=True, to=orm['demands.Ticket'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'demands', ['Ticket'])

        # Adding M2M table for field copy_to on 'Ticket'
        m2m_table_name = db.shorten_name(u'demands_ticket_copy_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm[u'demands.ticket'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticket_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Severity'
        db.delete_table(u'demands_severity')

        # Deleting model 'Priority'
        db.delete_table(u'demands_priority')

        # Deleting model 'Status'
        db.delete_table(u'demands_status')

        # Deleting model 'Domain'
        db.delete_table(u'demands_domain')

        # Deleting model 'SubDomain'
        db.delete_table(u'demands_subdomain')

        # Deleting model 'Ticket'
        db.delete_table(u'demands_ticket')

        # Removing M2M table for field copy_to on 'Ticket'
        db.delete_table(db.shorten_name(u'demands_ticket_copy_to'))


    models = {
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
        u'demands.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'demands.priority': {
            'Meta': {'object_name': 'Priority'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'demands.severity': {
            'Meta': {'object_name': 'Severity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'demands.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'demands.subdomain': {
            'Meta': {'object_name': 'SubDomain'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'subdomains'", 'to': u"orm['demands.Domain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'demands.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'created_tickets'", 'to': u"orm['auth.User']"}),
            'copy_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'followed_tickets'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demands.Domain']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_linked_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'related_tickets'", 'null': 'True', 'to': u"orm['demands.Ticket']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'parent_ticket': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['demands.Ticket']"}),
            'planned_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'planned_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'planned_workload': ('timedelta.fields.TimedeltaField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demands.Priority']", 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demands.Severity']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demands.Status']"}),
            'subdomain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demands.SubDomain']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['demands']