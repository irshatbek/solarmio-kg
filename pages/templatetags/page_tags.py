from django import template
from pages.models import *

register = template.Library()

@register.simple_tag()
def get_country():
    return Country.objects.all()