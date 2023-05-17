from django.shortcuts import render
from .models import Slide
from products.models import Product


def main(request):
    slider = Slide.objects.all()
    top_products = Product.objects.filter(show_on_main_page=True)
    print(request.session.get("cart"))
    return render(request, "index.html", {"slider": slider, "top_products": top_products})