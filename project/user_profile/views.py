from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, RetrieveUpdateAPIView
from user.models import User
from user_profile.models import UserProfile
from user_profile.serializers import UserSerializer
from user_profile.permissions import IsOwnerOrReadOnly


# Create your views here.

class RetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user
