from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageItemViewSet

router = DefaultRouter()
router.register(r'images', ImageItemViewSet, basename='imageitem')

urlpatterns = [
    path('', include(router.urls))
]