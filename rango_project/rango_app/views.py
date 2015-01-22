from django.shortcuts import render
from rango_app.models import Category
from rango_app.models import Page

from django.http import HttpResponse

def index(request):
   
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':page_list}
    return render(request, 'rango/index.txt', context_dict)

def about(request):
    context_dict = {'name': "Chris Brown", 'number': "2077762b" }
    return render(request, 'rango/about.txt', context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.txt', context_dict)
