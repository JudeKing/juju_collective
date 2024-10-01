from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=600)
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField()

    def __str__(self):
        return self.product_name