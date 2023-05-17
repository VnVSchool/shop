from django.db import models
from django.db.models import Q


class Product(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    discount_price = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    show_on_main_page = models.BooleanField(default=False)


    @property
    def main_image(self):
        return ProductImage.objects.filter(Q(product_id=self.id) & Q(is_main=True)).first()

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "discount_price": self.discount_price,
        }


    def __str__(self):
        return self.title


class ProductImage(models.Model):
    is_main = models.BooleanField()
    image = models.ImageField(upload_to="uploads/products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.id) + " " + self.product.title + "|" + str(self.id)
