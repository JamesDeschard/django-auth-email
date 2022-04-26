from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError

from login.registration_tools.password_generator import create_random_password
from login.registration_tools.email import send_confirmation_email


class User(AbstractUser):
    is_first_connection = models.BooleanField(default=False)


class EmailMessage(models.Model):
    title = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.title


class CreateNewUserProcedure(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
    def clean(self):
        unique_name = self.field_exists({'username':self.username})
        unique_email = self.field_exists({'email':self.email})

        if unique_name and unique_email:
            raise ValidationError(f'{self.username} and {self.email} are already in use!')
        elif unique_name:
            raise ValidationError(f'{self.username} is already in use!')
        elif unique_email:
            raise ValidationError(f'{self.email} is already in use!')

    def field_exists(self, query_field):
        return User.objects.filter(**query_field).exists()
    
    def send_confirmation_email(self, user, password):
        mail_status = send_confirmation_email(user, self.email, password)
        if mail_status == 1:
            return True, EmailMessage.objects.get(title='Success').message
        else:
            user.delete()
            return False, EmailMessage.objects.get(title='Error').message

    def create_new_user(self):
        password = create_random_password()  
                                
        user = User.objects.create_user(username=self.username,
                            email=self.email,
                            password=password) 
        user.is_active = False  
        user.save() 

        return self.send_confirmation_email(user, password)


    