from django.urls import path
from .views import PacientesList, PacienteEdit, PacienteDelete, PacienteNovo


urlpatterns = [
    path('', PacientesList.as_view(), name='list_pacientes'),
    path('editar/<int:pk>', PacienteEdit.as_view(), name='update_paciente'),
    path('delete/<int:pk>', PacienteDelete.as_view(), name='delete_paciente'),
    path('novo/', PacienteNovo.as_view(), name='create_paciente'),
]
