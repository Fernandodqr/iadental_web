from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from apps.pacientes.models import Paciente


def home(request):
    return render(request, 'core/index.html')

@login_required
def principal(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/principal.html', data)


