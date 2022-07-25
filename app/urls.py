from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.homepage, name="homepage"),

    
    # path('',views.login_signup),
    
]