from django.http import HttpResponseRedirect
from products.models import Product


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.session.get("cart", False):
        request.session["cart"] = []
    changed_quantity = False
    for cart_item in request.session.get("cart"):
        if cart_item["id"] == product.id:
            cart_item["quantity"]+=1
            changed_quantity = True
    if not changed_quantity:
        product_serialize = product.serialize()
        product_serialize["quantity"] = 1
        request.session["cart"].append(product_serialize)
    request.session.modified = True
    return HttpResponseRedirect("/")
