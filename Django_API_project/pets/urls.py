from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadView

router = DefaultRouter()
router.register(r"classify", ImageUploadView)

urlpatterns = [
    path('', include(router.urls))
]