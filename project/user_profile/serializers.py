from rest_framework import serializers
from user_profile.models import UserProfile
from django.contrib.auth import get_user_model
from user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'location')
        read_only_fields = ['updated_time', 'created_time']


class UserProfileCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'location', 'created_time', 'updated_time')


class UserProfilePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'location', 'created_time')


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileCrudSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'userprofile')

    def update(self, instance, validated_data):
        userprofile_data = validated_data.pop('userprofile', {})
        userprofile = instance.userprofile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        userprofile.location = userprofile_data.get('location', userprofile.location)
        userprofile.id = userprofile_data.get('id', userprofile.id)
        userprofile.save()

        return instance


class UserPublicSerializer(serializers.ModelSerializer):
    userprofile = UserProfilePublicSerializer()

    class Meta:
        model = User
        fields = ('username', 'userprofile')

    def update(self, instance, validated_data):
        userprofile_data = validated_data.pop('userprofile', {})
        userprofile = instance.userprofilepublic

        instance.username = validated_data.get('username', instance.username)
        instance.save()

        userprofile.location = userprofile_data.get('location', userprofile.location)
        userprofile.id = userprofile_data.get('id', userprofile.id)
        userprofile.save()

        return instance
