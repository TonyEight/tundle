# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Severity'
        db.create_table(u'tickets_severity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'tickets', ['Severity'])

        # Adding model 'Priority'
        db.create_table(u'tickets_priority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'tickets', ['Priority'])

        # Adding model 'Status'
        db.create_table(u'tickets_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'tickets', ['Status'])

        # Adding model 'Domain'
        db.create_table(u'tickets_domain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'tickets', ['Domain'])

        # Adding model 'SubDomain'
        db.create_table(u'tickets_subdomain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'subdomains', to=orm['tickets.Domain'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'tickets', ['SubDomain'])

        # Adding model 'Ticket'
        db.create_table(u'tickets_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'created_tickets', to=orm['auth.User'])),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Domain'], null=True, blank=True)),
            ('subdomain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.SubDomain'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Status'])),
            ('severity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Severity'], null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Priority'], null=True, blank=True)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('planned_workload', self.gf('timedelta.fields.TimedeltaField')(null=True, blank=True)),
            ('parent_ticket', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Ticket'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'tickets', ['Ticket'])

        # Adding M2M table for field copy_to on 'Ticket'
        m2m_table_name = db.shorten_name(u'tickets_ticket_copy_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm[u'tickets.ticket'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticket_id', 'user_id'])

        # Adding M2M table for field related_tickets on 'Ticket'
        m2m_table_name = db.shorten_name(u'tickets_ticket_related_tickets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_ticket', models.ForeignKey(orm[u'tickets.ticket'], null=False)),
            ('to_ticket', models.ForeignKey(orm[u'tickets.ticket'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_ticket_id', 'to_ticket_id'])


    def backwards(self, orm):
        # Deleting model 'Severity'
        db.delete_table(u'tickets_severity')

        # Deleting model 'Priority'
        db.delete_table(u'tickets_priority')

        # Deleting model 'Status'
        db.delete_table(u'tickets_status')

        # Deleting model 'Domain'
        db.delete_table(u'tickets_domain')

        # Deleting model 'SubDomain'
        db.delete_table(u'tickets_subdomain')

        # Deleting model 'Ticket'
        db.delete_table(u'tickets_ticket')

        # Removing M2M table for field copy_to on 'Ticket'
        db.delete_table(db.shorten_name(u'tickets_ticket_copy_to'))

        # Removing M2M table for field related_tickets on 'Ticket'
        db.delete_table(db.shorten_name(u'tickets_ticket_related_tickets'))


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
        u'tickets.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'tickets.priority': {
            'Meta': {'object_name': 'Priority'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'tickets.severity': {
            'Meta': {'object_name': 'Severity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'tickets.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'tickets.subdomain': {
            'Meta': {'object_name': 'SubDomain'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'subdomains'", 'to': u"orm['tickets.Domain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'tickets.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'created_tickets'", 'to': u"orm['auth.User']"}),
            'copy_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'followed_tickets'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Domain']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'parent_ticket': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Ticket']", 'null': 'True', 'blank': 'True'}),
            'planned_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'planned_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'planned_workload': ('timedelta.fields.TimedeltaField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Priority']", 'null': 'True', 'blank': 'True'}),
            'related_tickets': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_tickets_rel_+'", 'null': 'True', 'to': u"orm['tickets.Ticket']"}),
            'severity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Severity']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Status']"}),
            'subdomain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.SubDomain']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tickets']