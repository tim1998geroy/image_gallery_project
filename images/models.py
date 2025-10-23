from django.db import models

# Create your models here.

class ImageItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.CharField(max_length=255)
    cloudinary_public_id = models.CharField(255)
    uploaded_at = models.DateTimeField(auto_now_add=True)