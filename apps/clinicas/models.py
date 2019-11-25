from django.db import models
from django.contrib.auth.models import User



class Clinica(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=100, help_text='Telefone da empresa')
    address = models.CharField(max_length=100, help_text='Rua da empresa')
    CEP = models.CharField(max_length=100, help_text='CEP da empresa')
    City = models.CharField(max_length=100, help_text='Cidade da empresa')
    State = models.CharField(max_length=100, help_text='Estato da empresa')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

