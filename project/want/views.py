from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user_profile.models import UserProfile
from want.models import Want
from want.permissions import IsOwnerOrReadOnly
from want.serializers import WantSerializer
from want_image.models import WantImage


# Create your views here.


class ListAllWantsView(ListAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer
    permission_classes = []

    def get_queryset(self):
        title = self.request.query_params.get('title')
        tag = self.request.query_params.get('tag')
        if title or tag:
            objects = Want.objects.filter(title__icontains=title) if title else Want.objects.all()
            objects = objects.filter(tags=int(tag)) if tag else objects
            return objects.order_by('-created_time')[:10]
        else:
            objects = Want.objects.all().order_by('-created_time')[:10]
        return objects


class ListAndCreateWantsForLoggedInUserView(ListCreateAPIView):
    serializer_class = WantSerializer

    def perform_create(self, serializer):
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        images = self.request.FILES.getlist('images')
        instance = serializer.save(author=user_profile_of_user)
        for image in images:
            WantImage.objects.create(want=instance, images=image)

    def get_queryset(self):
        user = self.request.user
        user_profile_of_user = UserProfile.objects.get(user=user)
        return Want.objects.filter(author=user_profile_of_user).order_by('-created_time')


class RetrieveUpdateDeleteWantView(RetrieveUpdateDestroyAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):

        serializer.save()
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        images = self.request.FILES.getlist('images')
        instance = serializer.save(author=user_profile_of_user)
        for image in images:
            WantImage.objects.create(want=instance, images=image)

