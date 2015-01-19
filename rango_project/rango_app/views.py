from django.shortcuts import render

from django.http import HttpResponse

def index(request):
   
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.txt', context_dict)

def about(request):
    context_dict = {'name': "Chris Brown", 'number': "2077762b" }
    return render(request, 'rango/about.txt', context_dict)
