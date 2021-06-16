from django.urls import path
from tasashop import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('account/', views.account, name="account"),
    path('productdetails/', views.productdetails, name="productdetails"),
]
