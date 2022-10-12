from django.db import models

# from numpy import product
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Tables(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Tables name')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    

class Items(models.Model):  
    Tables = models.ForeignKey(Tables, verbose_name='Таблица', on_delete=models.CASCADE)
    сountry = models.CharField(max_length=255, verbose_name='Country')
    regions = models.CharField(max_length=255, verbose_name='regions')
    plant_name = models.CharField(max_length=255, verbose_name='plant_name')
    energies_category = models.CharField(max_length=255, verbose_name='energies_category')
    energy = models.CharField(max_length=255, verbose_name='energy')
    capacity = models.CharField(max_length=255, verbose_name='capacity')
    energy_generation = models.CharField(max_length=255, verbose_name='electricity_generation')
    Unit_name = models.CharField(max_length=255, verbose_name='Unit name')
    type_of_ownership = models.CharField(max_length=255, verbose_name='Type of ownership')
    operator = models.CharField(max_length=255, verbose_name='Operator')
    cost_ofenergy = models.CharField(max_length=255, verbose_name='cost_of_energy')

    def __str__(self):
        return self.title
   

class Parameter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    value = models.CharField(max_length=255, verbose_name="Значение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    item = models.ForeignKey(to=Items, verbose_name="Item", related_name="parameter", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.value}"



