from rest_framework import serializers

from user_profile.serializers import UserProfileSerializer
from have.models import Have


class HaveSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Have
        fields = (
            'id', 'author', 'tags', 'description', 'title', 'condition', 'wants_for_this_item', 'created_time',
            'updated_time')
        read_only_fields = ['id', 'created_time', 'updated_time']
