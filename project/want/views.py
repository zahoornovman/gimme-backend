from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView

from user_profile.models import UserProfile
from want.models import Want
from want.serializers import WantSerializer


# Create your views here.


class ListAllWants(ListAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer
    permission_classes = []

    def get_queryset(self):
        return Want.objects.all().order_by('-created_time')[:10]


class ListAndCreateWantsForLoggedInUser(ListCreateAPIView):
    serializer_class = WantSerializer

    def perform_create(self, serializer):
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        serializer.save(author=user_profile_of_user)

    def get_queryset(self):
        user = self.request.user
        user_profile_of_user = UserProfile.objects.get(user=user)
        return Want.objects.filter(author=user_profile_of_user)

