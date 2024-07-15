from django.http import HttpResponse
from django.shortcuts import render


def home():
    return HttpResponse('Teste')
