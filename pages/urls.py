from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country', views.country, name='country'),
    path('login', views.login, name='login'),
    path('login', views.login, name='login'),
    path('morris', views.morris, name='morris'),
    path('tables', views.tables, name='tables'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('chart', views.chart, name='chart'),
    path('<int:id>', views.table_detail, name='table_detail'),
    path('country_d/<int:id>', views.country_detail, name='country_detail'),



]
    
