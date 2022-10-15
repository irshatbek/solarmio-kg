from turtle import title
from django.db import models
from datetime import datetime
# from numpy import product
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


User = get_user_model()

class Country(models.Model):
    country_choice = (
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Tajikistan', 'Tajikistan'),
        
    )

    country_name = models.CharField(choices=country_choice, max_length=255)
    capital = models.CharField(max_length=255, verbose_name='capital', blank=True)
    country_area = models.CharField(max_length=255, verbose_name='country_area', blank=True)
    country_population = models.CharField(max_length=255, verbose_name='country_population', blank=True)
    country_currency = models.CharField(max_length=255, verbose_name='country_currency', blank=True)
    def __str__(self):
        return self.country_name

class Table(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Tables name')
    country_name = models.ForeignKey(Country,  max_length=255, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    

class Item(models.Model): 

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


    tables = models.ForeignKey(Table, verbose_name='Table name', on_delete=models.CASCADE, null=True, blank=True)
    country_name = models.ForeignKey(Country,  max_length=100, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='title', null=True)
    year = models.IntegerField(('year'), choices=year_choice, null=True)
    regions = models.CharField(max_length=255, verbose_name='regions', null=True, blank=True)
    plant_name = models.CharField(max_length=255, verbose_name='plant_name', null=True)
    energies_category = models.CharField(max_length=255, verbose_name='energies_category', null=True)
    energy = models.CharField(max_length=255, verbose_name='energy', null=True)
    capacity = models.CharField(max_length=255, verbose_name='capacity', null=True)
    energy_generation = models.CharField(max_length=255, verbose_name='electricity_generation', null=True)
    Unit_name = models.CharField(max_length=255, verbose_name='Unit name', null=True)
    type_of_ownership = models.CharField(max_length=255, verbose_name='Type of ownership', null=True)
    operator = models.CharField(max_length=255, verbose_name='Operator', null=True)
    cost_ofenergy = models.CharField(max_length=255, verbose_name='cost_of_energy', null=True)

    def __str__(self):
        return self.title
   

class Parameter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    value = models.CharField(max_length=255, verbose_name="Значение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    item = models.ForeignKey(to=Item, verbose_name="Item", related_name="parameter", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.value}"



