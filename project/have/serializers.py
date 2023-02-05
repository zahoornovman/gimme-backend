from rest_framework import serializers

from have.models import Have
from have_image.serializers import HaveImageSerializer
from user_profile.serializers import UserProfileSerializer


class HaveSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Have
        fields = (
            'id', 'author', 'tags', 'description', 'title', 'condition', 'wants_for_this_item', 'created_time',
            'updated_time')
        read_only_fields = ['id', 'created_time', 'updated_time']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = HaveImageSerializer(instance.images, many=True).data

        return representation
