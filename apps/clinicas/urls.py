from django.urls import path
from .views import ClinicaCreate, ClinicaEdit


urlpatterns = [
    path('novo', ClinicaCreate.as_view(), name='create_clinica'),
    path('editar/<int:pk>/',
         ClinicaEdit.as_view(), name='update_clinica'),
]
