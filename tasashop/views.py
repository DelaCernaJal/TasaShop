from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *


from django.contrib import messages


from django.http import JsonResponse
import json



@login_required(login_url='login_url')
def shop(request):	
	# category sort
	category = request.GET.get('category')
	if category == 'customizable':
		products = Product.objects.filter(category='c')
	elif category == 'designed':
		products = Product.objects.filter(category='d')
	else:
		products = Product.objects.all()

	# ordercount
	# if request.user.is_authenticated:
	customer = request.user	
	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	
	return render(request, 'shop.html', {'products':products, 'orderItem': orderItem})

# REGISTER/SIGNUP and LOGIN
def signupUser(request):
	page = 'signup'
	if request.user.is_authenticated:
		return redirect('shop')
	else:
		form = UserLoginForm()
		if request.method == 'POST':
			form = UserLoginForm(request.POST)
			if form.is_valid():

				user = form.save(commit=False)
				user.save()

				user = authenticate(
					request, username=user.username, password=request.POST['password1'])

				if user is not None:
					login(request, user)
					return redirect('shop')
		return render(request, 'login_signup.html', {'form':form, 'page': page})

def loginUser(request):
	page = 'login'
	if request.user.is_authenticated:
		return redirect('shop')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('shop')
			else:
				messages.info(request, 'Invalid Input')

		return render(request, 'login_signup.html', {'page': page})

def logoutUser(request):
	logout(request)
	return redirect('login_url')

def updateCart(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	user = request.user.id
	product = Product.objects.get(id=productId)
	order, created = OrderTrans.objects.get_or_create(customer=user, complete=False)	
	cartItem, created = CartItem.objects.get_or_create(order=order, product=product)
	
	if action == 'add':
		cartItem.quan = (cartItem.quan + 1)
	elif action == 'minus':
		cartItem.quan = (cartItem.quan - 1)

	cartItem.save()

	if cartItem.quan <= 0:
		cartItem.delete()

	if action == 'delete':
		cartItem.delete()
	return JsonResponse('Item Added', safe=False)




@login_required(login_url='login_url')
def cart(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
		cartlist = order.cartitem_set.all()
		img=Entries.objects.all()
	
	customer = request.user
	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	return render(request, 'cart.html', {'cartlist':cartlist,'img':img, 'orderItem': orderItem})


@login_required(login_url='login_url')
def checkout(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
		cartlist = order.cartitem_set.all()
	
	customer = request.user
	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	return render(request, 'checkout.html', {'orderItem': orderItem,'cartlist':cartlist, 'order': order})



@login_required(login_url='login_url')
def account(request):
	customer = request.user
	entry = request.GET.get('artby')
	if entry == None:
		userentry = Entries.objects.filter(artby=customer)
	img = Entries.objects.all()
	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	return render(request, 'account.html', {'img':img,'orderItem': orderItem, 'userentry':userentry} )


@login_required(login_url='login_url')
def entry(request):
	if request.method == "POST": 
		form=EntryForm(data=request.POST,files=request.FILES) 
		if form.is_valid(): 
			form.save()
			obj=form.instance 
			return render(request,"entry.html",{"obj":obj}) 
	else: 
		form=EntryForm()
	obj=form.instance 
	img=Entries.objects.all() 
	return render(request,"entry.html",{"img":img,"form":form, "obj":obj}) 




@login_required(login_url='login_url')
def productdetails(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == 'POST':
		product = Product.objects.get(id=pk)
		# product = .objects.get(id=pk)
		customer = request.user
		# artFile=request.POST['cdesign']		
		orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
		cartItem, created = CartItem.objects.get_or_create(order=orderItem, product=product)
		# cartItem = Entries_set.all(artFile=artFile)
		cartItem.quan = request.POST['quan']
		# cartItem.cdesign = request.POST['cdesign']
		cartItem.save()

		return redirect('cart')
	img=Entries.objects.all()
	customer = request.user
	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
	return render(request, 'productdetails.html', {'product':product, 'img':img, 'orderItem': orderItem })





# @login_required(login_url='login_url')
# def cdesign(request, pk):
# 	# product = Product.objects.get(id=pk)
	
# 	img=Entries.objects.get(id=pk)

# 	if request.method == 'POST':
# 		img=Entries.objects.get(id=pk)
# 		customer = request.user	
		
# 		orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
# 		cartItem, created = CartItem.objects.get_or_create(order=orderItem, product=product)
# 		cartItem.quan=request.POST['quan']
# 		cartItem.save()

# 		return redirect('cart')
# 	customer = request.user
# 	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
# 	return render(request, 'productdetails.html', {'product':product, 'img':img, 'orderItem': orderItem })

# def cdesign(request, pk):
# 	# entry = Entries.objects.get(id=pk)
	
# 	# img=Entries.objects.all()

# 	# if request.method == 'POST':
# 	# 	img = Entries.objects.get(id=pk)
	
# 	return render(request, 'cdesign.html')	


# if request.method == 'POST':
# 		form = EntryForm(request.POST)
# 		# if request.method == "POST": 
# 		# form=EntryForm(data=request.POST,files=request.FILES) 
# 		if form.is_valid(): 
# 			artentry = Entries()
# 			artentry.artprice = form.cleaned_data['artprice']
# 			artentry.artname = form.cleaned_data['artname']
# 			artentry.artfile = form.cleaned_data['artfile']
# 			artentry.artgcash = form.cleaned_data['artgcash']
# 			artentry.save()
			

# 			img = Entries.objects.all()
# 			# img.save() 
# 			# # obj=form.instance 
# 			return render (request,"account.html", {"img":img}) 
# 			# # else:
# 	# artby = request.user
# 	form=EntryForm()
# 	img = Entries.objects.all()
# 	customer = request.user
# 	orderItem, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
# 	return render(request,"entry.html", {'img':img,'form':form, 'orderItem': orderItem}) 



# def main(request):
# 	customer = request.user
# 	order, created = OrderTrans.objects.get_or_create(customer=customer, complete=False)
# 	cartlist = order.cartitem_set.all()
# 	return render(request, 'main.html', {'order': order})


# login

# class Customer(models.Model):
# 	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
# 	# Fname =  models.CharField(max_length=200, null=True)
# 	# Lname =  models.CharField(max_length=200, null=True)
# 	# email = models.EmailField(max_length=200, null=False)
# 	device = models.CharField(max_length=200, null=True)
# 	address = models.CharField(max_length=200, null=False)
# 	regis_on = models.DateTimeField(auto_now_add=True)

	
# 	@receiver(post_save, sender=User)
# 	def create_user_Customer(sender, instance, created, **kwargs):
# 		if created:
# 			Customer.objects.create(user=instance)

# 	@receiver(post_save, sender=User)
# 	def save_user_Customer(sender, instance, **kwargs):
# 		instance.customer.save()

# 	def __str__(self):
# 		return self.user



