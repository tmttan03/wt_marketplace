from django import forms
from django.conf import settings
from .models import StoreInvite

class InvitationForm(forms.ModelForm):
    invited = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = StoreInvite
        fields = ('invited', 'role')