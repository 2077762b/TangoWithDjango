from django.shortcuts import render
from rango_app.models import Category

from django.http import HttpResponse

def index(request):
   
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.txt', context_dict)

def about(request):
    context_dict = {'name': "Chris Brown", 'number': "2077762b" }
    return render(request, 'rango/about.txt', context_dict)
