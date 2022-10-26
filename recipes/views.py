from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': 'JOÃO MARCOS'
    })


def contato(request):
    return HttpResponse("Contato")


def sobre(request):
    return HttpResponse("Sobre")
