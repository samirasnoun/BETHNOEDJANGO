from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'BibleEnKabyle.html', views.BibleEnKabyleView, name='BibleEnKabyle'),
    
]
