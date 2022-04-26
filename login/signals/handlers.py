from django.db.models.signals import post_save
from django.dispatch import receiver

from login.models import CreateNewUserProcedure

@receiver(post_save, sender=CreateNewUserProcedure)
def create_new_user_model(sender, instance, **kwargs):
    instance.create_new_user()
    instance.delete()   
