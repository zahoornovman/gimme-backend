from rest_framework.generics import RetrieveUpdateDestroyAPIView

from want_image.permissions import IsOwnerOrReadOnly
from want_image.models import WantImage
from want_image.serializers import WantImageSerializer


# Create your views here.

class WantImageViewSet(RetrieveUpdateDestroyAPIView):
    queryset = WantImage.objects.all()
    serializer_class = WantImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
