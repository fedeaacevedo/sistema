from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.

def inicio(request):
    return HttpResponse("Fran te amo")

def nosotros(request):
    return render(request,('paginas/nosotros.html'))