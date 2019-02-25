from django import forms
from django.conf import settings
from .models import StoreInvite
from accounts.models import User

class InvitationForm(forms.ModelForm):
    invited = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = StoreInvite
        fields = ('invited', 'role')
    
    def clean_email(self):
        email = self.cleaned_data.get('invited')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email


class RegisterWithRoleForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('password','password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterWithRoleForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user