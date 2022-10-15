from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def country(request):
    tables = Table.objects.all()
    items = Item.objects.all()
    countres = Country.objects.all()
    
    data = {
        'tables': tables,
        'items': items,
        'countres': countres,

    }

    return render(request, 'pages/country.html', data)

def buttons(request):
    return render(request, 'pages/buttons.html')

def flot(request):
    return render(request, 'pages/flot.html')

def forms(request):
    return render(request, 'pages/forms.html')

def grid(request):
    return render(request, 'pages/grid.html')

def login(request):
    return render(request, 'pages/login.html')


def morris(request):
    return render(request, 'pages/morris.html')

def notifications(request):
    return render(request, 'pages/notifications.html')

def panels_wells(request):
    return render(request, 'pages/panels-wells.html')

def tables(request):
    tables = Table.objects.all()
    items = Item.objects.all()
    countres = Country.objects.all()
    
    data = {
        'tables': tables,
        'items': items,
        'countres': countres,

    }

    return render(request, 'pages/tables.html', data)

def sidebar(request):
    tables = Table.objects.all()
    items = Item.objects.all()
    countres = Country.objects.all()
    
    data = {
        'tables': tables,
        'items': items,
        'countres': countres,

    }

    return render(request, 'includes/sidebar.html', data)   

def typography(request):
    return render(request, 'pages/typography.html')

def table_detail(request, id):
    single_table = get_object_or_404(Table, pk=id)
    single_item = Item.objects.all()
    single_countres = get_object_or_404(Country, pk=id)


    data = {
        'single_table': single_table,
        'single_item': single_item,
        'single_countres': single_countres,
    }
    return render(request, 'pages/table_detail.html', data)

def country_detail(request, id):
    single_tables = Table.objects.all()
    single_item = Item.objects.all()
    single_countres = get_object_or_404(Country, pk=id)


    data = {
        'single_tables': single_tables,
        'single_item': single_item,
        'single_countres': single_countres,
    }
    return render(request, 'pages/country_detail.html', data)