from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.clinicas.models import Clinica
from apps.dentista.models import Dentista

class Paciente(models.Model):
    nome = models.CharField(max_length=100, help_text='Primeiro nome')
    sobrenome = models.CharField(max_length=100, help_text='Sobrenome')
    aniversario = models.CharField(max_length=100, help_text='Data de Aniversário')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=100, help_text='Telefone do Paciente')
    address = models.CharField(max_length=100, help_text='Rua')
    CEP = models.CharField(max_length=100, help_text='CEP')
    City = models.CharField(max_length=100, help_text='Cidade')
    State = models.CharField(max_length=100, help_text='Estado')
    dentistas = models.ManyToManyField(Dentista)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    clinicas = models.ForeignKey(Clinica, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_pacientes')

    def __str__(self):
        return self.nome
