from django.conf.urls import url
from . import views
from django.contrib import admin



urlpatterns = [
    url(r'EnseignementsBibliques/$', views.EnseignementsBibliquesView, name="EnseignementsBibliques"),  
    url(r'^EnseignementsBibliques/(?P<slug>[\w-]+)/$', 
    	views.EnseignementsBibliquesDetailView, name="EnseignementsBibliquesDetail"),


]
