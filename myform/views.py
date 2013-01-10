# Create your views here.
from django import forms
from django.core import serializers
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from myform.forms import ChickenForm
from myform.models import Animal, Species
from django.contrib.gis.shortcuts import render_to_text
import pprint
from recaptcha.client import captcha
from django.utils import translation
import formtest.tools

def chicken(request):
    captcha_error = ''
    if request.method == 'POST':
        form = ChickenForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('myform.views.result'))
    else:
        form = ChickenForm()
        
    return render_to_response('myform/chicken.html', 
                              {'form': form, 
                               'captcha_error':captcha_error,
                               'lang':translation.get_language()}, 
                              context_instance=RequestContext(request))
    
def index(request):
    return HttpResponse('Index page')

def result(request):
    #pprint.pprint(request.POST)
    return HttpResponse('result page: ')

def findAnimal(request, searchString):
    
    try:
        output = list(Animal.objects.filter(name__contains=searchString).values_list('name', flat=True))
    except:
        output =  []
        
    return formtest.tools.json_response(output)

def speciesLookup(request, lookup):
    try:
        output = list(Species.objects.filter(name__contains=lookup).extra(select={ 'label':"name || '_' || diet", 'value':'name'}).values('label', 'value'))
    except Exception, err:
        pprint.pprint(err)
        output = []
        
    return formtest.tools.json_response(output)
    
def ajaxtest(request):
    if request.is_ajax():
        return HttpResponse('Hello ajax!')
    return HttpResponse('Hello normal request!')
    
    