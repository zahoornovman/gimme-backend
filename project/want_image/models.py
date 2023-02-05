from django.db import models

from want.models import Want


def post_directory_path(instance, filename):
    print(instance)
    return f'{instance.want.author.id}/{filename}'


# Create your models here.

class WantImage(models.Model):
    want = models.ForeignKey(to=Want, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    images = models.ImageField(upload_to=post_directory_path, blank=True, null=True)

    def __str__(self):
        return f'ID: {self.id}: Want Image for UserProfile {self.images}'
