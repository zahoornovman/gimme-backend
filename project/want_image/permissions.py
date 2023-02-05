from rest_framework import permissions

from user_profile.models import UserProfile


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        user_profile_of_user = UserProfile.objects.get(user=request.user)
        return obj.want.author == user_profile_of_user
