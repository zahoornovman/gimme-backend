from django.db import models

from have.models import Have
from user_profile.models import UserProfile
from want.models import Want


# Create your models here.

class Message(models.Model):
    receiver = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    sender = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.CharField(max_length=300)
    receiver_have = models.ForeignKey(to=Have, on_delete=models.CASCADE, related_name='received_messages_for_have',
                                      null=True, blank=True)
    sender_have = models.ForeignKey(to=Have, on_delete=models.CASCADE, related_name='sent_messages_for_have', null=True,
                                    blank=True)
    receiver_want = models.ForeignKey(to=Want, on_delete=models.CASCADE, related_name='received_messages_for_want',
                                      null=True, blank=True)
    sender_want = models.ForeignKey(to=Want, on_delete=models.CASCADE, related_name='sent_messages_for_want', null=True,
                                    blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message sent from: {self.receiver.id} to {self.sender.id}'
