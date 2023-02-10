from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from have.models import Have
from have.permissions import IsOwnerOrReadOnly
from have.serializers import HaveSerializer
from have_image.models import HaveImage
from user_profile.models import UserProfile


# Create your views here.
class ListAllHavesView(ListAPIView):
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
    permission_classes = []

    def get_queryset(self):
        title = self.request.query_params.get('title')
        tag = self.request.query_params.get('tag')
        if title or tag:
            objects = Have.objects.filter(status__in=(1, 2), title__icontains=title) if title else Have.objects.all()
            objects = objects.filter(tags=int(tag)) if tag else objects
            return objects.order_by('-created_time')[:10]
        else:
            objects = Have.objects.filter(status__in=(1, 2)).order_by('-created_time')[:10]
        return objects


class ListAndCreateHavesForLoggedInUserView(ListCreateAPIView):
    serializer_class = HaveSerializer

    def perform_create(self, serializer):
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        images = self.request.FILES.getlist('images')
        instance = serializer.save(author=user_profile_of_user)
        for image in images:
            HaveImage.objects.create(have=instance, images=image)

    def get_queryset(self):
        user = self.request.user
        user_profile_of_user = UserProfile.objects.get(user=user)
        return Have.objects.filter(author=user_profile_of_user).order_by('-created_time')


class RetrieveUpdateDeleteHaveView(RetrieveUpdateDestroyAPIView):
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        images = self.request.FILES.getlist('images')
        instance = serializer.save(author=user_profile_of_user)
        for image in images:
            HaveImage.objects.create(have=instance, images=image)
