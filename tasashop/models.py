from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Entries(models.Model):
	artby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	artgcash = models.DecimalField(max_digits=11, decimal_places=0, default=0)
	artprice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	artname = models.CharField(max_length=200, null=True)
	artfile = models.ImageField(null=True, blank=True)
	
	def __str__(self):
		return self.artname

	def artURL(self):
		try:
			art = self.artfile.url
		except:
			art = ''
		return art

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	PRODUCT_LABEL = (
					('c', 'customizable'),
					('d', 'designed')
					)
	category = models.CharField(choices=PRODUCT_LABEL,max_length=1, null=True)
	description = models.CharField(max_length=5000, null=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	def imgurl(self):
		try:
			img = self.image.url
		except:
			img = ''
		return img

class OrderTrans(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def cart_total(self):
		order = self.cartitem_set.all()
		computation = sum([item.total for item in order])
		return computation

	@property
	def cart_item(self):
		order = self.cartitem_set.all()
		computation = sum([item.quan for item in order])
		return computation


class CartItem(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(OrderTrans, on_delete=models.SET_NULL, null=True)
	quan = models.IntegerField(default=0, null=True, blank=True)
	cdesign = models.ForeignKey(Entries, on_delete=models.SET_NULL, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def total(self):
		computation = self.product.price * self.quan
		return computation

class Shipping(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(OrderTrans, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)