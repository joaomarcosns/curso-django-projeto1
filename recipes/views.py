from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Home")


def contato(request):
    return HttpResponse("Contato")


def sobre(request):
    return HttpResponse("Sobre")
