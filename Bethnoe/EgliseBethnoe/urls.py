from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from admin import adminEgliseBethnoe





urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    # url(r'^adminEgliseBethnoe/', include(adminEgliseBethnoe.urls)),
    url(r'^adminEB/', adminEgliseBethnoe.urls),
    url(r'^admin/', admin.site.urls),

   
]


print adminEgliseBethnoe.urls


# This is only needed when using runserver.
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
