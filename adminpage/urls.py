from django.contrib import admin
from django.urls import path,include
from adminpage import views

urlpatterns = [
    path('',views.adminlogin),
    path('home',views.adminhome),
    path('addproducts',views.addproducts),
    path('add',views.add),

    
    # path('',views.login_signup),
    
]