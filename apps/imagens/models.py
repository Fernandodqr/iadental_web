from django.db import models
from django.shortcuts import reverse
from apps.pacientes.models import Paciente


class Imagens(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='imagens')

    def get_absolute_url(self):
        return reverse("update_paciente", args=[self.pertence.id])

    def __str__(self):
        return self.descricao
