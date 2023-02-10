from django.db import models

from tag.models import Tag
from user_profile.models import UserProfile


# Create your models here.

class Want(models.Model):
    class Conditions(models.IntegerChoices):
        NEW = 1
        USED_LIKE_NEW = 2
        USED_GOOD = 3
        USED_FAIR = 4

    class Status(models.IntegerChoices):
        ACTIVE = 1
        PENDING = 2
        NOT_ACTIVE = 3
        FOUND = 4

    author = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='wants')
    tags = models.ManyToManyField(to=Tag, related_name='wants')
    description = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=100, blank=False)
    condition = models.IntegerField(choices=Conditions.choices, blank=True)
    status = models.IntegerField(choices=Status.choices, blank=False)
    has_for_this_item = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}'

