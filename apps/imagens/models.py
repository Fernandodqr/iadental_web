from django.db import models
from apps.pacientes.models import Paciente


class Imagens(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
