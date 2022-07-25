from django.contrib import admin
from django.urls import path,include
from adminpage import views

urlpatterns = [
    path('',views.adminlogin, name="adminlogin"),
    path('home',views.adminhome, name="adminhome"),
    path('order',views.order, name="order"),
 
    path('logout',views.logoutadmin),
    path('addproducts',views.addproducts, name="addproducts"),
    path('add',views.add, name="add"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('delete_order/<int:id>',views.delete_order),
    
    path('edit/<int:id>/', views.edit ,name="edit"),
    path('updatepage/<int:id>', views.updatepage, name="updatepage")

    
    # path('',views.login_signup),
    
]