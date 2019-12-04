from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Detection
from apps.pacientes.models import Paciente
from apps.imagens.models import Imagens

class DetectionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Detection
        fields = '__all__'

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ImagensSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = '__all__'
