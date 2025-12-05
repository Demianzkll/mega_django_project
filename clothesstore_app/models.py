from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,          
        blank=False             
    )
    brand = models.CharField(
        max_length=10,
        blank=True,             
        null=True
    )
    size = models.CharField(
        max_length=4,
        blank=False             
    )
    color = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    price = models.IntegerField(
        default=0,             
        help_text="Ціна у гривнях"
    )

