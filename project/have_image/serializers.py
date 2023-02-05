from rest_framework import serializers

from have_image.models import HaveImage


class HaveImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaveImage
        fields = '__all__'
