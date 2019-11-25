from django.db import models


class Dentista(models.Model):
    nome = models.CharField(max_length=100, help_text='Primeiro nome do Dentista')
    crm = models.CharField(max_length=100, help_text='CRM Dentista')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=100, help_text='Telefone do Paciente')
    address = models.CharField(max_length=100, help_text='Rua')
    CEP = models.CharField(max_length=100, help_text='CEP')
    City = models.CharField(max_length=100, help_text='Cidade')
    State = models.CharField(max_length=100, help_text='Estado')

    def __str__(self):
        return self.nome
