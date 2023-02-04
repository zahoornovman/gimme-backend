from rest_framework import serializers

from user_profile.serializers import UserProfileSerializer
from want.models import Want
from want_image.serializers import WantImageSerializer


class WantSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    # images = WantImageSerializer(many=True, allow_null=True)

    class Meta:
        model = Want
        fields = (
            'id', 'author', 'tags', 'description', 'title', 'condition', 'has_for_this_item', 'created_time',
            'updated_time')
        read_only_fields = ['id', 'created_time', 'updated_time']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = WantImageSerializer(instance.images, many=True).data
        # self.request.data.get('images')

        return representation

