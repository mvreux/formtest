from django.conf.urls import url, patterns
from django.views.generic import ListView, DetailView
from myform.models import Animal, Species, Individual

urlpatterns = patterns('',
                       url(r'^$', 
                           ListView.as_view(
                                model=Animal,
                                template_name='myform/index.html'        
                           )
                       ),
                       url(r'^animal/(?P<pk>\d+)/$',
                           DetailView.as_view(
                                model=Animal,
                                template_name='myform/animal.html'
                           )
                       ),
                       url(r'^chicken$', 'myform.views.chicken'),
                       url(r'^result$',  'myform.views.result'),
                       url(r'^ajaxtest$','myform.views.ajaxtest'),
                       url(r'^species/lookup/(?P<lookup>.*)/', 'myform.views.speciesLookup'),
                       url(r'^find/animal/(?P<searchString>.*)/', 'myform.views.findAnimal'),
              )