from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'BibleEnKabyle.html', views.BibleEnKabyleView, name='BibleEnKabyle'),
    # url(r'BibleEnKabyle_lecture/', views.BibleEnKabyleLectureView, name='BibleEnKabyle_lecture'),
    url(r'^BibleEnKabyle_lecture/(?P<slug>[\w-]+)/$', views.BibleEnKabyleLectureView, name='BibleEnKabyleLectureView'),

]
