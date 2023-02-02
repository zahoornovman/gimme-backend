from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user_profile.models import UserProfile
from want.models import Want
from want.permissions import IsOwnerOrReadOnly
from want.serializers import WantSerializer


# Create your views here.


class ListAllWantsView(ListAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer
    permission_classes = []

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title']

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return Want.objects.filter(title__icontains=search).order_by('-created_time')

        return Want.objects.all().order_by('-created_time')[:10]


class ListAndCreateWantsForLoggedInUserView(ListCreateAPIView):
    serializer_class = WantSerializer

    def perform_create(self, serializer):
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        serializer.save(author=user_profile_of_user)

    def get_queryset(self):
        user = self.request.user
        user_profile_of_user = UserProfile.objects.get(user=user)
        return Want.objects.filter(author=user_profile_of_user).order_by('-created_time')


class RetrieveUpdateDeleteWantView(RetrieveUpdateDestroyAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer
    permission_classes = [IsOwnerOrReadOnly]
