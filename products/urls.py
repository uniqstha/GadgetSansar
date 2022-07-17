from django.urls import path,include
from products import views
urlpatterns = [

    path("phone",views.phone),
    path("audio",views.audio),
    path("power",views.power),
    path("fitness",views.fitness),
    path('phone/productdetails/<int:id>',views.phoneDetails),
    path('audio/productdetails/<int:id>',views.audioDetails),
    path('power/productdetails/<int:id>',views.powerDetails),
    path('fitness/productdetails/<int:id>',views.fitnessDetails),
    # cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    # checkout
    path("checkout",views.checkout),
    # order
    path("order",views.order),
    path("search",views.search),
    
 
]