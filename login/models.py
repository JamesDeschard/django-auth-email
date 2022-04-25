from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_first_connection = models.BooleanField(default=False)

class CreateNewUserProcedure(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=128)