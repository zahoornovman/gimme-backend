from django.db import models

from have.models import Have
from user_profile.models import UserProfile
from want.models import Want


# Create your models here.

class Message(models.Model):
    receiver = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    sender = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.CharField(max_length=300)
    have = models.ForeignKey(to=Have, on_delete=models.CASCADE, related_name='messages')
    want = models.ForeignKey(to=Want, on_delete=models.CASCADE, related_name='messages')
