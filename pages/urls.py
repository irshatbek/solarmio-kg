from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country', views.country, name='country'),
    path('about', views.about, name='about'),
    path('tables', views.tables, name='tables'),
    path('search', views.search, name='search'),
    path('navbar', views.navbar, name='navbar'),
    path('<int:table_id>', views.table_detail, name='table_detail'),
    path('country_d/<int:country_id>/', views.country_detail, name='country_detail'),




]
    
