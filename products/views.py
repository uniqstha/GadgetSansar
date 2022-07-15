import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

from products.models import Product

# Create your views here.
def phone(request):
    # products=Products.objects.all()
    products = Product.objects.filter(productCategory='phone').values()
    return render(request, 'phones.html' ,{'products': products, 'nbar':'phone'})

def phoneDetails(request,id):
    products=Product.objects.get(id=id)
    return render(request, "productDetails/phoneDetails.html",{'products':products,'nbar':'phone'})

def audio(request):
    # products=Products.objects.all()
    products = Product.objects.filter(productCategory='audio').values()
    return render(request, 'audio.html' ,{'products': products, 'nbar':'audio'})

def audioDetails(request,id):
    products=Product.objects.get(id=id)
    return render(request, "productDetails/audioDetails.html",{'products':products,'nbar':'audio'})

def power(request):
    # products=Products.objects.all()
    products = Product.objects.filter(productCategory='power').values()
    return render(request, 'power.html' ,{'products': products, 'nbar':'power'})

def powerDetails(request,id):
    products=Product.objects.get(id=id)
    return render(request, "productDetails/powerDetails.html",{'products':products,'nbar':'power'})

def fitness(request):
    # products=Products.objects.all()
    products = Product.objects.filter(productCategory='fitness').values()
    return render(request, 'fitness.html' ,{'products': products, 'nbar':'fitness'})

def fitnessDetails(request,id):
    products=Product.objects.get(id=id)
    return render(request, "productDetails/fitnessDetails.html",{'products':products,'nbar':'fitness'})
def cart(request):
    return render(request, "cart.html")



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/users/loginsignup")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/loginsignup")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/loginsignup")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/loginsignup")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="//users/loginsignup")
def cart_detail(request):
    return render(request, 'cart.html')

