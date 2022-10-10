from django.shortcuts import render


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

def motifications(request):
    return render(request, 'pages/motifications.html')

def panels_wells(request):
    return render(request, 'pages/panels-wells.html')

def tables(request):
    return render(request, 'pages/tables.html')

def typography(request):
    return render(request, 'pages/typography.html')

