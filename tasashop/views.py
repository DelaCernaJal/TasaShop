from django.shortcuts import render
from tasashop.models import *


# Create your views here.
def shop(request):
	# price sort
	
	# category sort
	category = request.GET.get('category')
	if category == 'customizable':
		products = Product.objects.filter(category='c')
	elif category == 'designed':
		products = Product.objects.filter(category='d')
	else:
		products = Product.objects.all()

	# para sa bilog sa carticon in navbar
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	else:
		order = {'cart_total':0, 'cart_item':0}

	return render(request, 'shop.html', {'products':products, 'order': order})


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
		cartlist = order.cartitem_set.all()
	else:
		cartlist = []
		order = {'cart_total':0, 'cart_item':0}
	return render(request, 'cart.html', {'cartlist':cartlist, 'order': order})

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
		cartlist = order.cartitem_set.all()
	else:
		cartlist = []
		order = {'cart_total':0, 'cart_item':0}
	return render(request, 'checkout.html', {'cartlist':cartlist, 'order': order})


def account(request):
	return render(request, 'account.html')

def productdetails(request):
	return render(request, 'productdetails.html')
