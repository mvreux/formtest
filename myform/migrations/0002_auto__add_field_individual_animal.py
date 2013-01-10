# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Individual.animal'
        db.add_column('myform_individual', 'animal',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['myform.Animal']),
                      keep_default=False)

        # Adding M2M table for field animals on 'Species'
        db.create_table('myform_species_animals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('species', models.ForeignKey(orm['myform.species'], null=False)),
            ('animal', models.ForeignKey(orm['myform.animal'], null=False))
        ))
        db.create_unique('myform_species_animals', ['species_id', 'animal_id'])


    def backwards(self, orm):
        # Deleting field 'Individual.animal'
        db.delete_column('myform_individual', 'animal_id')

        # Removing M2M table for field animals on 'Species'
        db.delete_table('myform_species_animals')


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
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myform.Animal']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'myform.species': {
            'Meta': {'object_name': 'Species'},
            'animals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myform.Animal']", 'symmetrical': 'False'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['myform']