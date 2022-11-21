from django.contrib import admin
from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['tables', 'title', 'year', 'regions', 'plant_name', 'energies_category', 'energy', 'capacity', 'energy_generation', 'Unit_name', 'type_of_ownership', 'operator', 'cost_ofenergy']
    list_editable = ['title', 'year', 'regions', 'plant_name', 'energies_category', 'energy', 'capacity', 'energy_generation', 'Unit_name', 'type_of_ownership', 'operator', 'cost_ofenergy']
    ordering = ['tables']
    
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("country_name",)}
    
class TableAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Country, CountryAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Parameter)

