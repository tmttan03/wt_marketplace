from django import forms
from .models import Product, Category, ProductAlbum
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from places.fields import PlacesField

class PostForm(forms.ModelForm):
	name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder':'What are you selling?'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe your item', 'rows':'3'}), label='')
	price = forms.DecimalField(max_digits=10, decimal_places=2, label='', widget=forms.TextInput(attrs={'placeholder':'Price'}))
	category = forms.ModelChoiceField(Category.objects.all(), label='')
	location= forms.CharField(label='',widget=forms.TextInput(attrs={'onFocus':'geolocate()','autocomplete':'off', 'placeholder':'Location'}))
	class Meta:
		model = Product
		fields = ['is_draft','name','price','location','category','description']


class ImageFieldForm(forms.Form):
    img_field = forms.ImageField()

    class Meta:
    	model = ProductAlbum
    	fields = ['img_field'] 