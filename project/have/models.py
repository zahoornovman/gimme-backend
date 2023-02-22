from django.db import models

from tag.models import Tag
from user_profile.models import UserProfile


# Create your models here.

class Have(models.Model):
    class Conditions(models.IntegerChoices):
        NEW = 1
        USED_LIKE_NEW = 2
        USED_GOOD = 3
        USED_FAIR = 4

    class Status(models.IntegerChoices):
        ACTIVE = 1
        PENDING = 2
        NOT_ACTIVE = 3
        GONE = 4

    author = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='haves')
    tags = models.ManyToManyField(to=Tag, related_name='haves')
    description = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=100, blank=False)
    condition = models.IntegerField(choices=Conditions.choices, blank=False)
    status = models.IntegerField(choices=Status.choices, blank=False)
    wants_for_this_item = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}'