# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Profile.hide_getting_started'
        db.alter_column('profile_profile', 'hide_getting_started', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Profile.has_setup_feeds'
        db.alter_column('profile_profile', 'has_setup_feeds', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Profile.has_trained_intelligence'
        db.alter_column('profile_profile', 'has_trained_intelligence', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Profile.has_found_friends'
        db.alter_column('profile_profile', 'has_found_friends', self.gf('django.db.models.fields.NullBooleanField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Profile.hide_getting_started'
        db.alter_column('profile_profile', 'hide_getting_started', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Profile.has_setup_feeds'
        db.alter_column('profile_profile', 'has_setup_feeds', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Profile.has_trained_intelligence'
        db.alter_column('profile_profile', 'has_trained_intelligence', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Profile.has_found_friends'
        db.alter_column('profile_profile', 'has_found_friends', self.gf('django.db.models.fields.BooleanField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profile.profile': {
            'Meta': {'object_name': 'Profile'},
            'collapsed_folders': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'feed_pane_size': ('django.db.models.fields.IntegerField', [], {'default': '240'}),
            'has_found_friends': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'has_setup_feeds': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'has_trained_intelligence': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'hide_getting_started': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'hide_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_seen_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_seen_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'preferences': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'secret_token': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'send_emails': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stripe_4_digits': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'timezone': ('vendor.timezones.fields.TimeZoneField', [], {'default': "'America/New_York'", 'max_length': '100'}),
            'tutorial_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'view_settings': ('django.db.models.fields.TextField', [], {'default': "'{}'"})
        }
    }

    complete_apps = ['profile']
