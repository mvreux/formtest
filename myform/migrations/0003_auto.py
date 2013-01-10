# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field species on 'Animal'
        db.create_table('myform_animal_species', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('animal', models.ForeignKey(orm['myform.animal'], null=False)),
            ('species', models.ForeignKey(orm['myform.species'], null=False))
        ))
        db.create_unique('myform_animal_species', ['animal_id', 'species_id'])

        # Removing M2M table for field animals on 'Species'
        db.delete_table('myform_species_animals')


    def backwards(self, orm):
        # Removing M2M table for field species on 'Animal'
        db.delete_table('myform_animal_species')

        # Adding M2M table for field animals on 'Species'
        db.create_table('myform_species_animals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('species', models.ForeignKey(orm['myform.species'], null=False)),
            ('animal', models.ForeignKey(orm['myform.animal'], null=False))
        ))
        db.create_unique('myform_species_animals', ['species_id', 'animal_id'])


    models = {
        'myform.animal': {
            'Meta': {'object_name': 'Animal'},
            'averageLifeSpan': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'species': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myform.Species']", 'symmetrical': 'False'})
        },
        'myform.individual': {
            'Meta': {'object_name': 'Individual'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myform.Animal']"}),
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