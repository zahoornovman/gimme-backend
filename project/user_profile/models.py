from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='userprofile')
    location = models.CharField(blank=True, max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
