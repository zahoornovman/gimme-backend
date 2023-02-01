from rest_framework import serializers

from user_profile.serializers import UserProfileSerializer
from want.models import Want


class WantSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    # author = serializers.ReadOnlyField(source='author.user.username')

    class Meta:
        model = Want
        fields = (
            'id', 'author', 'tags', 'description', 'title', 'condition', 'has_for_this_item', 'created_time',
            'updated_time')
        read_only_fields = ['id', 'created_time', 'updated_time']
