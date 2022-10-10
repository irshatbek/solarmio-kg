from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blank', views.blank, name='blank'),
    path('buttons', views.buttons, name='buttons'),
    path('flot', views.flot, name='flot'),
    path('forms', views.forms, name='forms'),
    path('grid', views.grid, name='grid'),
    path('login', views.login, name='login'),
    path('login', views.login, name='login'),
    path('morris', views.morris, name='morris'),
    path('motifications', views.motifications, name='motifications'),
    path('panels_wells', views.panels_wells, name='panels_wells'),
    path('tables', views.tables, name='tables'),
    path('typography', views.typography, name='typography'),

]
    