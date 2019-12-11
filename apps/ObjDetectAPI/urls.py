from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from apps.ObjDetectAPI import views
from apps.ObjDetectAPI.views import APIView, api_detection_view, PacienteViewSet, ImagensViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'detection', views.DetectionView)
router.register(r'paciente', views.PacienteViewSet)
router.register(r'imagens', views.ImagensViewSet)


urlpatterns = [
    path('teste/', APIView.as_view(), name='api_view'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('pacientes/detail/external/', views.external, name='external'),
    path('detect/', api_detection_view, name='detect'),
    #path('', ObjDetectAPI.site.urls),
    #path('', .as_view(), name='detectionAPI'),
]
