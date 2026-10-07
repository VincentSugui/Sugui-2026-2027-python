from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageFiel(upload_to="user/avatar/")
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username