from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Clinica


class ClinicaCreate(CreateView):
    model = Clinica
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        paciente = self.request.user.paciente
        paciente.clinicas = obj
        paciente.save()
        return HttpResponse('ok')


class ClinicaEdit(UpdateView):
    model = Clinica
    fields = ['nome',
              'email',
              'phone',
              'address'
]
