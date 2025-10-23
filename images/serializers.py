from rest_framework import serializers
from .models import ImageItem

class ImageItemSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(write_only= True)

    class Meta:
        model = ImageItem
        fields = [
            'id', 
            'title', 
            'description', 
            'image_url',
            'cloudinary_public_id',
            'uploaded_at', 
            'file'
            ]

        read_only_fields = [
            'id',
            'image_url',
            'cloudinary_public_id',
            'uploaded_at'
        ]
