from rest_framework.generics import RetrieveUpdateDestroyAPIView

from have_image.models import HaveImage
from have_image.permissions import IsOwnerOrReadOnly
from have_image.serializers import HaveImageSerializer


# Deleting image
class HaveImageDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = HaveImage.objects.all()
    serializer_class = HaveImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
