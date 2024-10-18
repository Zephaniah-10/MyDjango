from django.db import models

# Create your models here.

class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    image_src = models.CharField(max_length=255 , blank=True , null=True)
    # quantity

    def __str__(self):
        return f'{self.pk} {self.name} - {self.price}'
    


