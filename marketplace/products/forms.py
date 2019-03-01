from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

from .models import Product, Category, ProductAlbum, Stock, Comment

class PostForm(forms.ModelForm):
	name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder':'What are you selling?'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe your item', 'rows':'3'}), label='')
	price = forms.DecimalField(max_digits=10, decimal_places=2, label='', widget=forms.TextInput(attrs={'placeholder':'Price'}))
	category = forms.ModelChoiceField(Category.objects.all(), label='')
	location= forms.CharField(label='',widget=forms.TextInput(attrs={'onFocus':'geolocate()','autocomplete':'off', 'placeholder':'Location'}))
	class Meta:
		model = Product
		fields = ['name','price','location','category','description']


class UpdatePostForm(forms.ModelForm):
	name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder':'What are you selling?'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe your item', 'rows':'3'}), label='')
	price = forms.DecimalField(max_digits=10, decimal_places=2, label='', widget=forms.TextInput(attrs={'placeholder':'Price'}))
	category = forms.ModelChoiceField(Category.objects.all(), label='')
	location= forms.CharField(label='',disabled=True)

	class Meta:
		model = Product
		fields = ['name','price','location','category','description']


class ImageFieldForm(forms.Form):
    img_field = forms.ImageField()

    class Meta:
    	model = ProductAlbum
    	fields = ['img_field'] 


class StockForm(forms.ModelForm):
	stock_total = forms.IntegerField(label='Total Stocks Available',widget=forms.TextInput(attrs={'min':'1','type':'number','value':1}))
	
	class Meta:
		model = Stock
		fields = ['stock_total']

class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write a Comment', 'rows':'2'}), label='')

	class Meta:
		model = Comment
		fields = ['comment']

		
class UpdateCommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write a Comment', 'rows':'1'}), label='')

	class Meta:
		model = Comment
		fields = ['comment']

		