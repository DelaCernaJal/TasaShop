from django.urls import path
from tasashop.views import *

# from .views import *
# from tasashop.views import *

urlpatterns = [
    path('', shop, name="shop"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('account/', account, name="account"),
    path('entry/', entry, name="entry"),


    path('updateCart/', updateCart, name="updateCart"),




    path('productdetails/<str:pk>/', productdetails, name="productdetails"),


    # path("register/", registerUser, name="register"),

    

    path('signup/', signupUser, name='signup_url'),
    path('login/', loginUser, name='login_url'),
    path('logout/', logoutUser, name='logout_url'),

    

    path('cdesign/', cdesign, name='cdesign'),


    # path("CustomerLogout/", CustomerLogout.as_view(), name="CustomerLogout"),
    # path("CustomerLogout/", CustomerLogin.as_view(), name="CustomerLogout"),



]
