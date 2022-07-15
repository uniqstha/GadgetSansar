from django.contrib import admin
from django.urls import path,include
from adminpage import views

urlpatterns = [
    path('',views.adminlogin),
    path('home',views.adminhome),
    path('addproduct',views.addproduct),

    
    # path('',views.login_signup),
    
]