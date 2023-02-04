# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from want_image.permissions import IsOwnerOrReadOnly
from .models import WantImage
from .serializers import WantImageSerializer


class WantImageViewSet(RetrieveUpdateDestroyAPIView):
    queryset = WantImage.objects.all()
    serializer_class = WantImageSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # @action(detail=True, methods=['delete'])
    # def delete_image(self, request):
    #     print(request)
    #     obj = self.get_object(pk=request.data.id)
    #     obj.image.delete()
    #     obj.save()
    #     return Response({"message": "Image deleted successfully"})

