from contextvars import Context
from django.http import HttpResponse
from django.template import Context, Template, loader

def inicio(request):
    return HttpResponse("Esta es mi familia:")

def codigohtml(self):
    nom="Giuliana"
    ape="Barreto"
    Lista_nombres=["Giuliana", "Silvina", "Pampa"]
    diccionario={'nombre':nom, 'apellido':ape, 'lista_nombres':Lista_nombres}


    template=loader.get_template("template1.html")
    
    documento=template.render(diccionario)

    return HttpResponse(documento)