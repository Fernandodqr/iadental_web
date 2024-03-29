from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('apps.core.urls')),
    path('pacientes/', include('apps.pacientes.urls')),
    path('clinica/', include('apps.clinicas.urls')),
    path('imagem/', include('apps.imagens.urls')),
    path('api/', include('apps.ObjDetectAPI.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
