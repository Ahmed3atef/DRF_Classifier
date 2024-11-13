# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ImageUploadSerializer
from .models  import ImageUpload
from .utils import trained_model

class ImageUploadView(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            instance = serializer.save()
            result = trained_model(instance.image.path)
            return Response(result)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
