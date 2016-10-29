from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'EgliseBethnoe/', views.IndexEgliseBethnoeView, name="indexEgliseBethnoe"),
    url(r'EgliseBethnoe.html', views.IndexView, name="index"),
    # url(r'^adminEgliseBethnoe/', include(adminEgliseBethnoe.urls)),   
    url(r'^admin/', admin.site.urls),   
]

# This is only needed when using runserver.
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
