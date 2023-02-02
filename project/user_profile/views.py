from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from user_profile.permissions import IsOwnerOrReadOnly


# Create your views here.

class RetrieveUpdateDeleteUserProfileView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        return queryset
