from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary.uploader import upload as cloud_upload
from cloudinary.exceptions import Error as Cloud_Error

from .models import ImageItem
from .serializers import ImageItemSerializer

class ImageItemViewSet(viewsets.ModelViewSet):
    queryset = ImageItem.objects.all().order_by('-uploaded_at')
    serializer_class = ImageItemSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description', '')
        image_file = request.FILES.get('image')

        if not title:
            return Response({'error': 'Поле "title" обязательно'}, status=status.HTTP_400_BAD_REQUEST)

        if not image_file:
            return Response({'error': 'Необходимо прикрепить файл изображения'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            upload_result = cloud_upload(image_file)

            image_item = ImageItem.objects.create(
                title=title,
                description=description,
                image_url=upload_result.get('secure_url'),
                public_id=upload_result.get('public_id')
            )

            serializer = self.get_serializer(image_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:  # или CloudError, если импортирован
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# Create your views here.


 