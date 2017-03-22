from django.conf.urls import url
from . import views
from django.contrib import admin




urlpatterns = [

    url(r'EnseignementsBibliques/$', 
    	views.EnseignementsBibliques, name="EnseignementsBibliques"),  
    
    url(r'^EnseignementsBibliques/(?P<slug>[\w-]+)/$', 
     	views.EnseignementsBibliquesDetailView, name="EnseignementsBibliquesDetail"),
    
    url(r'EglisesPartenaires/$', 
    	views.EglisesPartenairesView, name="EglisesPartenaires"),
    
    url(r'^EglisesPartenaires/(?P<slug>[\w-]+)/$', 
     	views.EglisesPartenairesDetailView, name="EglisesPartenairesDetail"),


]
 