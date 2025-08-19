from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def user_created_handler(sender,instance,created,*args,**kwargs):
    if created:
        print("Send an email ",instance.username)
    else:
        print(instance.username," Is just saved")