from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [

    url(r'BibleEnKabyle/(?P<ecoute_lecture>[\w-]+)/$', views.BibleEnKabyleView, name="BibleEnKabyle"),  
    url(r'^BibleEnKabyle_lecture/(?P<slug>[\w-]+)/$', 
    	views.BibleEnKabyleLectureView, name="BibleEnKabyleLecture"),
    url(r'^BibleEnKabyle_ecoute/(?P<slug>[\w-]+)/$', 
    	views.BibleEnKabyleEcouteView, name="BibleEnKabyleEcoute"), 

]