from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.name
