from django.conf.urls import url
from . import views
from django.contrib import admin



urlpatterns = [

    url(r'^EtudesBibliques/$', 
    	views.EtudesBibliquesView, name="EtudesBibliques"),

    url(r'^EtudesBibliques/(?P<slug>[\w-]+)/$', 
    	views.EtudesBibliquesDetailView, name="EtudesBibliquesDetail"),



]
