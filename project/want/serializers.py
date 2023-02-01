from rest_framework import serializers

from user_profile.serializers import UserProfileSerializer
from want.models import Want


class WantSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Want
        fields = (
            'id', 'user_profile', 'tags', 'description', 'title', 'condition', 'has_for_this_item', 'updated_time')
        read_only_fields = ['id', 'created_time', 'updated_time']
