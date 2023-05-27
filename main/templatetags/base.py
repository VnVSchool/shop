import datetime
from django import template
from products.models import Product

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag
def top_products():
    return Product.objects.filter(show_on_main_page=True)