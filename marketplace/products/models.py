from django.db import models

#from accounts.models import Store
from places.fields import PlacesField
from PIL import Image

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title 


class Product(models.Model):
	DELETED = '0'
	AVAILABLE = '1'
	SOLD = '2'

	STATUS_CHOICES = (
		(DELETED, "Deleted"),
		(AVAILABLE, "Available"),
		(SOLD, "Sold"),
	)

	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	location = PlacesField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	#seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="store_owner")
	#store = models.ForeignKey(Store, on_delete=models.CASCADE)
	is_draft = models.BooleanField(default=False)
	#stock_on_hand = models.PositiveIntegerField(default=1)
	status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class ProductAlbum(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='product_images/',default='no-thumb.png')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name + " Image"

	