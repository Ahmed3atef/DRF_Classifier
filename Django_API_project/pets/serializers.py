from rest_framework import serializers
from .models import ImageUpload

class ImageUploadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ImageUpload
        fields ="__all__"
