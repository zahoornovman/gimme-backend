from django.db import models

from have.models import Have


def post_directory_path(instance, filename):
    return f'{instance.want.author.id}/{filename}'


# Create your models here.

class HaveImage(models.Model):
    have = models.ForeignKey(to=Have, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to=post_directory_path, blank=True, null=True)

    def __str__(self):
        return f'ID: {self.id}: Have Image for UserProfile {self.images}'

