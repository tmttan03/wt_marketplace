from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from store.models import Store

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_owner:
        store = Store(owner=instance)
        store.save()

    
