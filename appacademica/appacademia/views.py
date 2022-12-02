from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def saludo(request):
    return HttpResponse("Hola Mundo")

def edad(request, edad):
    return HttpResponse("Mi edad es: %s" % edad)

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())