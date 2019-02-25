import uuid

from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=128, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="store")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f'{self.owner.get_short_name()} Store'

    def save(self, *args, **kwargs):
        self.name = '{}-Store'.format(self.owner.get_short_name())
        super().save(*args, **kwargs)
        

class StoreMembers(models.Model):
    STAFF = '0'
    MODERATOR = '1'
    
    ROLE_CHOICES = (
        (STAFF, 'Staff'),
        (MODERATOR, 'Moderator')
    )

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="members")
    members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="members")
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=STAFF)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.store.name} - {self.members.get_short_name()}-{ self.role }'


class StoreInvite(models.Model):
    STAFF = '0'
    MODERATOR = '1'
    
    ROLE_CHOICES = (
        (STAFF, 'Staff'),
        (MODERATOR, 'Moderator')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="invite")
    invited = models.EmailField()
    token = models.CharField(max_length=150) 
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=STAFF)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.token = uuid.uuid4()
        super().save(*args,**kwargs)

