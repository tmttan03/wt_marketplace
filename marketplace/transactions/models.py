from products.models import Product , Category
from django.conf import settings
from django.db import models


class Transaction(models.Model):
	SOLD = '0'
	PENDING = '1'

	STATUS_CHOICES = (
		(SOLD, "Sold"),
		(PENDING, "Pending"),
	)
	no = models.CharField(max_length=100)
	buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transaction")
	status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
	start_transaction = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.no

class Order(models.Model):
	INACTIVE = '0'
	ACTIVE = '1'
	
	STATUS_CHOICES = (
		(INACTIVE, "Inactive"),
		(ACTIVE, "Active"),
	)
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	reference_no = models.CharField(max_length=100)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.PositiveIntegerField(default=1)
	comment = models.CharField(max_length=500)
	status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    
	def __str__(self):
		return self.reference_no


class Payment(models.Model):
	no = models.CharField(max_length=100)
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	amount_due = models.DecimalField(max_digits=10, decimal_places=2)
	purchased_date = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.no

