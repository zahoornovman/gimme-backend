from django.db import models


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


