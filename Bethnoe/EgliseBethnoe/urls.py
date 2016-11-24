from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'EgliseBethnoe/$', views.IndexEgliseBethnoeView, name="indexEgliseBethnoe"),

    url(r'EgliseBethnoe/evenements/(?P<slug>[\w-]+)/$', views.IndexEgliseBethnoeEvenementsDetailView, name="IndexEgliseBethnoeEvenementsDetail"),
    url(r'EgliseBethnoe/posts/(?P<slug>[\w-]+)/$', views.IndexEgliseBethnoePostsDetailView, name="IndexEgliseBethnoePostsDetail"),
    url(r'EgliseBethnoe/piere/(?P<slug>[\w-]+)/$', views.IndexEgliseBethnoePriereDetailView, name="IndexEgliseBethnoePrieresDetail"),

    url(r'EgliseBethnoe.html', views.IndexView, name="index"),
    url(r'EgliseBethnoe/evenements/$', views.IndexEgliseBethnoeEvenementsView, name="IndexEgliseBethnoeEvenements"),
    url(r'EgliseBethnoe/espacemembers/$', views.IndexEgliseBethnoeEspaceMembersView, name="IndexEgliseBethnoeEspaceMembers"),
    url(r'EgliseBethnoe/confession-de-foie/$', views.IndexEgliseBethnoeConfessionFoieView, name="IndexEgliseBethnoeConfessionFoie"),
    
    url(r'EgliseBethnoe/forum/', views.IndexForumView, name="IndexForum"),
    url(r'EgliseBethnoe/contact/', views.contact, name="Contact"),
    url(r'EgliseBethnoe/Louanges/$', views.LouangesView, name="Louange"),
    url(r'EgliseBethnoe/Louanges/(?P<slug>[\w-]+)/$', views.LouangesLectureView, name="louange_lecture"),
    url(r'EgliseBethnoe/Posts/$', views.PostsView, name="Post"),
    url(r'EgliseBethnoe/Prieres/$', views.PrieresView, name="Priere"),
    url(r'EgliseBethnoe/liens/$', views.ChapitreLiensView, name="liens"),
    url(r'EgliseBethnoe/inscription/', views.AddUser, name="add_user"),

    url(r'^admin/', admin.site.urls),   
]

# This is only needed when using runserver.
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


