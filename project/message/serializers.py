from rest_framework import serializers

from have.serializers import HaveSerializer
from message.models import Message
from user_profile.serializers import UserProfileSerializer
from want.serializers import WantSerializer


class MessageSerializer(serializers.ModelSerializer):
    receiver = UserProfileSerializer(read_only=True)
    sender = UserProfileSerializer(read_only=True)
    have = HaveSerializer(read_only=True)
    want = WantSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'receiver', 'sender', 'content', 'have', 'want')
        read_only_fields = ['id', 'created_time']
