from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Product(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')