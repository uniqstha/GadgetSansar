from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from products.forms import ProductsForm

from products.views import Product

# Create your views here.
def adminlogin(request):
    if (request.method=="POST"):
        em=request.POST['em']
        
        ps=request.POST['ps']
        
        user=authenticate(request,username=em,password=ps)

        if user is not None:
            if user.is_superuser == 1:
                login(request,user)
                return redirect('/admin/home')
            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin')
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")

    else:
        return render(request, 'admin/adminlogin.html')
    
def adminhome(request):
    products = Product.objects.all()
    audio = Product.objects.all()
    power = Product.objects.all()
    fitness = Product.objects.all()
    return render(request, 'admin/adminhome.html' ,{'products': products,'audio': audio,'power': power,'fitness': fitness, 'nbar':'home'})

def addproducts(request):
    return render(request, "admin/addproduct.html")

def add(request):
    data = ProductsForm(request.POST, request.FILES)
    print(request.POST)
    data.save()
    return redirect('/admin/item')

def logoutadmin(request):
    logout(request)
    return redirect("/")