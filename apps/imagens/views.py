from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import reverse
from .models import Imagens



class ImageCreate(CreateView):
    model = Imagens
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['paciente_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('update_paciente', args=[self.kwargs['paciente_id']])
