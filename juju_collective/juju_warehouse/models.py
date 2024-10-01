from django.db import models

# Create your models here.
class Product(models.Model):
    """Represents a product with its name, description, price and image.
        
        Attributes:
            product_name (str): The name of the product.
            product_description (str): The description of the product.
            product_price (int): The price of the product.
            product_image (ImageField): The image of the product.

        Methods:
            __str__(): Returns the name of the product.
    """
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=600)
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField()

    def __str__(self):
        return self.product_name