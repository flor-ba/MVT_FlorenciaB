from django.shortcuts import render
from .models import Familia

# Create your views here.

def crear_integrante(self):
    integrante1=Familia(nombre="Giuliana", edad=21, fecha_nacimiento="2001-2-12")
    context = {'integrante1':integrante1}
    integrante1.save()

    return render(self, 'template1.html', context)