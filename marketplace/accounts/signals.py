from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Store, User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        store = Store()
        store.user = instance
        store.save()
        
