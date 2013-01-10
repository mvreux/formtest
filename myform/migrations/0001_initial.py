# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Species'
        db.create_table('myform_species', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('diet', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('myform', ['Species'])

        # Adding model 'Animal'
        db.create_table('myform_animal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('averageLifeSpan', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('myform', ['Animal'])

        # Adding model 'Individual'
        db.create_table('myform_individual', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('myform', ['Individual'])


    def backwards(self, orm):
        # Deleting model 'Species'
        db.delete_table('myform_species')

        # Deleting model 'Animal'
        db.delete_table('myform_animal')

        # Deleting model 'Individual'
        db.delete_table('myform_individual')


    models = {
        'myform.animal': {
            'Meta': {'object_name': 'Animal'},
            'averageLifeSpan': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'myform.individual': {
            'Meta': {'object_name': 'Individual'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'myform.species': {
            'Meta': {'object_name': 'Species'},
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['myform']