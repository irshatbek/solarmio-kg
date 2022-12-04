from django.shortcuts import get_object_or_404, render
from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, ListView
# Create your views here.

def country(request):
    tables = Table.objects.all()
    countre = Country.objects.all() 
    data = {
        'tables': tables,
        'countre': countre,
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
    country = get_object_or_404(Country, pk=country_id)
    data = {
        'tables': tables,
        'country': country,
    }
    return render(request, 'pages/country_detail.html', data)



def filter_search(request):
        
    # other filter search
    tables = Table.objects.all().order_by("-id")

    country_name_search = Table.objects.values_list('table_country', flat=True).distinct()
    year_search = Table.objects.values_list('year', flat=True).distinct()
    energy_type_search = Table.objects.values_list('energy_type', flat=True).distinct()
    

    if 'energy_type' in request.GET:
        type = request.GET['energy_type']
        if type:
            tables = tables.filter(energy_type__iexact=type)
    
    if 'year' in request.GET:
        year_t = request.GET['year']
        if year_t:
            tables = tables.filter(year__iexact=year_t)

    if 'table_country' in request.GET:
        city = request.GET['table_country']
        if city:
            tables = tables.filter(table_country__iexact=city)
         
    data = {
        'tables': tables,
        'country_name_search': country_name_search,
        'year_search': year_search,
        'energy_type_search': energy_type_search,
    }
    return render(request, 'pages/filter_search.html', data)
    
