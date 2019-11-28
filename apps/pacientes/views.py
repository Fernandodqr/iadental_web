from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Paciente, Clinica


class PacientesList(ListView):
    model = Paciente


#    def get_queryset(self):
#        clinica_logada = self.request.user.paciente.clinicas
#        return Paciente.objects.filter(clinica=clinica_logada)

class PacienteEdit(UpdateView):
    model = Paciente
    fields = ['nome', 'sobrenome', 'clinicas']

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('list_pacientes')

class PacienteNovo(CreateView):
    model = Paciente
    fields = ['nome', 'sobrenome', 'clinicas']

    def form_valid(self, form):
        paciente = form.save(commit=False)
        username = paciente.nome.split(' ')[0]+paciente.nome.split(' ')[1]
        paciente.clinicas = self.request.user.paciente.clinicas
        paciente.user = User.objects.create(username=username)
        paciente.save()
        return super(PacienteNovo, self).form_valid(form)
