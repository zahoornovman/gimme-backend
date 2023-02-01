from django.db import models

from want.models import Want


# Create your models here.

class WantImage(models.Model):
    want = models.ForeignKey(to=Want, on_delete=models.CASCADE, related_name='images')
