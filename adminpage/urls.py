from django.contrib import admin
from django.urls import path,include
from adminpage import views

urlpatterns = [
    path('',views.adminlogin),

    
    # path('',views.login_signup),
    
]