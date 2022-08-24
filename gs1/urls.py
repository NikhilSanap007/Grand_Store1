from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart_detail', views.cart_detail, name="cart_detail"),

### remove comment for sending contact details to mail ###
#    path('contact', views.ContactUs, name="contact"),

### remove comment for storing data to database ###
    path('contact', views.contact, name="contact"),

    #Add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
