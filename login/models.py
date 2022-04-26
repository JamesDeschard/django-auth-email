from django.db import models
from django.contrib.auth.models import AbstractUser

from login.registration_tools.password_generator import create_random_password
from login.registration_tools.email import send_confirmation_email

class User(AbstractUser):
    is_first_connection = models.BooleanField(default=False)

class CreateNewUserProcedure(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def create_new_user(self):
        password = create_random_password()   
        user = User.objects.create_user(username=self.username,
                                email=self.email,
                                password=password) 
        user.is_active = False  
        user.save() 
        send_confirmation_email(user, self.email, password)
        return True

    