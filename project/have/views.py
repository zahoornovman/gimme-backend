from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from have.models import Have
from have.permissions import IsOwnerOrReadOnly
from have.serializers import HaveSerializer
from user_profile.models import UserProfile


# Create your views here.
class ListAllHavesView(ListAPIView):
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
    permission_classes = []

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return Have.objects.filter(title__icontains=search).order_by('-created_time')

        return Have.objects.all().order_by('-created_time')[:10]


class ListAndCreateHavesForLoggedInUserView(ListCreateAPIView):
    serializer_class = HaveSerializer

    def perform_create(self, serializer):
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        serializer.save(author=user_profile_of_user)

    def get_queryset(self):
        user = self.request.user
        user_profile_of_user = UserProfile.objects.get(user=user)
        return Have.objects.filter(author=user_profile_of_user).order_by('-created_time')


class RetrieveUpdateDeleteHaveView(RetrieveUpdateDestroyAPIView):
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
    permission_classes = [IsOwnerOrReadOnly]
