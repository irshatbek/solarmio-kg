from django.shortcuts import get_object_or_404, render
from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, ListView
# Create your views here.

def country(request):
    tables = Table.objects.all()
    items = Item.objects.all() 
    data = {
        'tables': tables,
        'items': items,
    }
    return render(request, 'pages/country.html', data)

def about(request):
    tables = Table.objects.all()
    items = Item.objects.all()  
    data = {
        'tables': tables,
        'items': items,}
    return render(request, 'pages/about.html', data)

def home(request):
    tables = Table.objects.all()
    items = Item.objects.all()  
    data = {
        'tables': tables,
        'items': items,
    }
    return render(request, 'pages/home.html', data)

def tables(request):
    tables = Table.objects.all()
    items = Item.objects.all()  
    data = {
        'tables': tables,
        'items': items,
    }
    return render(request, 'pages/tables.html', data)

def navbar(request):
    tables = Table.objects.all()
    items = Item.objects.all()
    data = {
        'tables': tables,
        'items': items,
    }
    return render(request, 'includes/navbar.html', data)   

def table_detail(request, table_id):
    tables = get_object_or_404(Table, pk=table_id)
    items = Item.objects.all()
    data = {
        'tables': tables,
        'items': items,
    }
    return render(request, 'pages/table_detail.html', data)

def country_detail(request, country_id):
    tables = Table.objects.all()
    items = Item.objects.all()
    country = get_object_or_404(Country, pk=country_id)
    data = {
        'tables': tables,
        'items': items,
        'country': country,
    }
    return render(request, 'pages/country_detail.html', data)

def search(request):
    search_post = request.GET.get('q')
    items = Item.objects.all() 

    if search_post:
        posts = Table.objects.filter(Q(name__icontains=search_post) | Q(description__icontains=search_post))
    else:
       
        posts = Table.objects.all().order_by("-id")  
    return render(request, 'pages/search.html', {'posts': posts, 'items': items,})
    
    

