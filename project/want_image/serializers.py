from rest_framework import serializers

from want_image.models import WantImage


class WantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantImage
        fields = '__all__'
