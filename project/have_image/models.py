from django.db import models

from have.models import Have


# Create your models here.

class HaveImage(models.Model):
    have = models.ForeignKey(to=Have, on_delete=models.CASCADE, related_name='images')
