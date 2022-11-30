from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country', views.country, name='country'),
    path('about', views.about, name='about'),
    path('table/<int:table_id>/', views.table_detail, name='table_detail'),
    path('country/<int:country_id>/', views.country_detail, name='country_detail'),
    path('filter_search', views.filter_search, name='filter_search'),


]
    
