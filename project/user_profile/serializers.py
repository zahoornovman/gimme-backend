from rest_framework import serializers

from user_profile.models import UserProfile
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user_ser = UserSerializer(instance=user, data=user_data)
        if user_ser.is_valid():
            user_ser.save()

        instance.location = validated_data.get('location', instance.location)
        instance.save()

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'location', 'email', 'last_name', 'first_name')
        read_only_fields = ['updated_time', 'created_time']
