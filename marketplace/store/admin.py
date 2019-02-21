from django.contrib import admin
from store.models import Store, StoreMembers, StoreInvite

# Register your models here.
admin.site.register(Store)
admin.site.register(StoreMembers)
admin.site.register(StoreInvite)