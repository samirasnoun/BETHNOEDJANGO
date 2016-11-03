from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'EgliseBethnoe/$', views.IndexEgliseBethnoeView, name="indexEgliseBethnoe"),

    url(r'EgliseBethnoe/evenements/(?P<slug>[\w-]+)/$', views.IndexEgliseBethnoeEvenementsDetailView, name="IndexEgliseBethnoeEvenementsDetail"),

    url(r'EgliseBethnoe.html', views.IndexView, name="index"),
    url(r'EgliseBethnoe/evenements/$', views.IndexEgliseBethnoeEvenementsView, name="IndexEgliseBethnoeEvenements"),
    url(r'EgliseBethnoe/espacemembers/$', views.IndexEgliseBethnoeEspaceMembersView, name="IndexEgliseBethnoeEspaceMembers"),
    
    url(r'EgliseBethnoe/forum/', views.IndexForumView, name="IndexForum"),


    url(r'^admin/', admin.site.urls),   
]

# This is only needed when using runserver.
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


