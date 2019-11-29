from django.urls import path
from .views import ImageCreate

urlpatterns = [
    path('novo/<int:paciente_id>/', ImageCreate.as_view(), name='create_image'),
    # path('editar/<int:pk>', PacienteEdit.as_view(), name='update_paciente'),
    # path('delete/<int:pk>', PacienteDelete.as_view(), name='delete_paciente'),
    # path('novo/', PacienteNovo.as_view(), name='create_paciente'),
]
