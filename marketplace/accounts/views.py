from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import RegisterForm,UpdateUserForm,UserAdminCreationForm, UserAdminChangeForm
from products.models import Product, Category, ProductAlbum, Stock, Comment
# Create your views here.

class RegisterView(TemplateView):
	"""Register a New User"""
	template_name = 'accounts/register.html'
	form = RegisterForm
	
	def get_context_data(self, **kwargs):
		context = super(RegisterView, self).get_context_data(**kwargs)
		context['form'] = self.form()
		return context
		
	def post(self,*args,**kwargs):
		form = self.form(self.request.POST)
		
		if form.is_valid():
			form.save()
			messages.success(self.request, f'Your account has been created! You are now able to login.')
			return redirect('login')     
		return render(self.request, self.template_name,{'form': form})


class UpdateUserView(LoginRequiredMixin, TemplateView):
	"""Update the logged in user"""
	template_name = 'accounts/edit-profile.html'
	
	def get_context_data(self, **kwargs):
		context = super(UpdateUserView, self).get_context_data(**kwargs)
		context['form'] = UpdateUserForm(instance=self.request.user)
		return context
		
	def post(self,*args,**kwargs):
		form = UpdateUserForm(self.request.POST, self.request.FILES, instance=self.request.user)
		if form.is_valid():
			form.save()
			messages.success(self.request, f'Your account has been updated!')
			return redirect('login')     
		return render(self.request, self.template_name,{'form': form})









