import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    service = models.CharField(max_length=255)
    experience = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.photo:
            # Generate a unique filename
            file_ext = os.path.splitext(self.photo.name)[1]
            unique_filename = f'products/{self.name}-{uuid.uuid4().hex[:8]}{file_ext}'
            
            # Save the file to storage
            file_name = default_storage.save(unique_filename, ContentFile(self.photo.read()))
            
            # Update the photo field to the new path
            self.photo = file_name
        
        super().save(*args, **kwargs)