"""Bethnoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),  
    url(r'^', include('EgliseBethnoe.urls', namespace='EgliseBethnoe')),
    url(r'^', include('BibleEnKabyle.urls', namespace='BibleEnKabyle')),
    url(r'^', include('EtudesBibliques.urls', namespace='EtudesBibliques')),
    url(r'^', include('EnseignementsBibliques.urls', namespace='EnseignementsBibliques')),
    url(r'accounts/login/', views.login, name="login"),
    url(r'accounts/resetpassword/', views.password_reset, name="password_reset"),
    url(r'^resetpassword/passwordsent/', views.password_reset_done, name='password_reset_done'),


    #url(r'^publisher-polls/', include('polls.urls', namespace='publisher-polls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


