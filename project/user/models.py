from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    # field used for registration and authorization
    USERNAME_FIELD = 'email'

    # required for createsuperuser script
    REQUIRED_FIELDS = ['username']

    # they can be only one user with an email
    email = models.EmailField(unique=True)

    def str(self):
        return f"ID: {self.id} Email: {self.email}"
