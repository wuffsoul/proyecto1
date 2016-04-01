from django.shortcuts import render
from django.http import HttpResponse

def listar_post(request):
    return HttpResponse("<h1>Listar</h1>")

def crear_post(request):
    return HttpResponse("<h1>Crear</h1>")

def detalle_post(request):
    return HttpResponse("<h1>Detalle</h1>")

def actualizar_post(request):
    return HttpResponse("<h1>Actualizar</h1>")

def borrar_post(request):
    return HttpResponse("<h1>Borrar</h1>")
