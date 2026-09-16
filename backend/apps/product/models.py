from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Molde del producto almacenado en la base de datos
    """
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_cost = models.DateTimeField(max_length=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    