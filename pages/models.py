from django.db import models
from datetime import datetime
# from numpy import product
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse




User = get_user_model()

class Country(models.Model):

    country_name = models.CharField(max_length=255, verbose_name='Country name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    capital = models.CharField(max_length=255, verbose_name='capital', blank=True)
    country_area = models.CharField(max_length=255, verbose_name='country_area', blank=True)
    country_population = models.CharField(max_length=255, verbose_name='country_population', blank=True)
    country_currency = models.CharField(max_length=255, verbose_name='country_currency', blank=True)
    about_country = models.TextField(blank=True, verbose_name='about_country', null=True)
    energe_info = models.TextField(blank=True, verbose_name='energe_info', null=True)
    country_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_description = models.TextField(blank=True, verbose_name='photo_description', null=True)
    country_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description_1 = models.TextField(blank=True, verbose_name='photo_description_1', null=True)
    country_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description_2 = models.TextField(blank=True, verbose_name='photo_description_2', null=True)
    country_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description_3 = models.TextField(blank=True, verbose_name='photo_description_3', null=True)

    
    
    def __str__(self):
        return self.country_name
    
    def get_absolute_url(self):
        return reverse('country', kwargs={'country_id': self.pk})

class Table(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Table name')
    country_name = models.ForeignKey(Country,  max_length=255, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, verbose_name='description', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    table_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description = models.TextField(blank=True, verbose_name='photo_description', null=True)
    table_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description_1 = models.TextField(blank=True, verbose_name='photo_description_1', null=True)
    table_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_description_2 = models.TextField(blank=True, verbose_name='photo_description_2', null=True)
    source = models.TextField(blank=True, verbose_name='source', null=True)

    
    def get_absolute_url(self):
        return reverse('table', kwargs={'table_id': self.pk})
    
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
    capacity = models.FloatField(verbose_name='capacity', null=True)
    energy_generation = models.FloatField(verbose_name='electricity_generation', null=True)
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



