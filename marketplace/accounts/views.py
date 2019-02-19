from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			password = form.cleaned_data.get('password')
			print(password)
			messages.success(request, f'Your account has been created! You are now able to login.')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html',{'form': form})