from django.urls import path
from .views import home, principal


urlpatterns = [
    path('', home, name='home'),
    path('principal', principal, name='principal'),
]
