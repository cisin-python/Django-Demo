# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('social_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('article_type', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('social', ['Article'])

        # Adding model 'Comment'
        db.create_table('social_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', blank=True, to=orm['social.Article'], null=True)),
            ('commenter', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('social', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('social_article')

        # Deleting model 'Comment'
        db.delete_table('social_comment')


    models = {
        'social.article': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Article'},
            'article_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'social.comment': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'blank': 'True', 'to': "orm['social.Article']", 'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'commenter': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['social']