import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    service = models.CharField(max_length=255)
    experience = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.CharField(max_length=255)
    stock = models.IntegerField()
    additional_experience = models.TextField()

    def __str__(self):
        return self.name

class Id(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
