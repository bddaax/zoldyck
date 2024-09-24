import uuid
from django.db import models
from django.contrib.auth.models import User

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name