from django.db import models
from django import forms
from django.utils.translation import ugettext as _

# Create your models here.
    
class Species(models.Model):
    DIET_CHOICES = (
                        ('C', _('Carnivore')),
                        ('V', _('Veggetarian')),
                        ('H', _('Herbivore'))
                    )
    name = models.CharField(max_length=200)
    diet = models.CharField(max_length=1, choices=DIET_CHOICES)
    def __unicode__(self):
        return self.name

class Animal(models.Model):
    species = models.ManyToManyField(Species)
    name = models.CharField(max_length=200)
    averageLifeSpan = models.IntegerField('Average lifespan')
    def __unicode__(self):
        return self.name
    
class Individual(models.Model):
    GENDER_CHOICES = (
                        ('M', 'Male'),
                        ('F', 'Female'),
                      )
    animal = models.ForeignKey(Animal)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #gender.widget = forms.RadioSelect
    age = models.IntegerField()
    def __unicode__(self):
        return self.name
