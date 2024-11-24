from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name