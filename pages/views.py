from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def blank(request):
    return render(request, 'pages/blank.html')

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
    
    data = {
        'tables': tables,
        'items': items,

    }
    # tables = Table.objects.all()
    # data = {
    #     'tables': tables,
    # }
    return render(request, 'pages/tables.html', data)

def typography(request):
    return render(request, 'pages/typography.html')

