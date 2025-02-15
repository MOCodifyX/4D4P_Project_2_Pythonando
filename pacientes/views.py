from django.shortcuts import render
from django.http import HttpResponse

def pacientes(request):
    return render(request, 'pacientes.html')
