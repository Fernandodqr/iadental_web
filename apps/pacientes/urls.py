from django.urls import path
from apps.pacientes import views
from .views import (PacientesList, PacienteUpdate, Pdf,
                    PacienteDelete,
                    PacienteNovo,
                    PacienteDetail)


urlpatterns = [
    path('', PacientesList.as_view(), name='list_pacientes'),
    #path('editar/<int:pk>', PacienteEdit.as_view(), name='edit_pacientes'),
    path('update/<int:pk>', PacienteUpdate.as_view(), name='update_pacientes'),
    path('delete/<int:pk>', PacienteDelete.as_view(), name='delete_paciente'),
    path('novo/', PacienteNovo.as_view(), name='create_pacientes'),
    path('detail/<int:pk>', PacienteDetail.as_view(), name='detail_paciente'),
    #path('detect/<id>/', views.detect, name='detect'),
    path('detect/<id>/', views.detect, name='detect'),
    path('laudo_paciente_html/', Pdf.as_view(), name='laudo_paciente_html'),
    #path('editdetection/', views.EditDetect, name='edit_detect'),
]

