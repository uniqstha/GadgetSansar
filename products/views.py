from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from orders.models import Order

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



@login_required(login_url="/user/loginsignup")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/user/loginsignup")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/user/loginsignup")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/user/loginsignup")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/user/loginsignup")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/user/loginsignup")
def cart_detail(request):
    return render(request, 'cart.html')

def checkout(request):
    if request.method=="POST":
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        payment=request.POST.get('payment')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=(float(cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b

            order=Order(
                user=user,
                productBrand=cart[i]['brand'],
                name=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                phonenumber=phonenumber,
                email=email,
                address=address,
                pincode=pincode,
                payment=payment,
                total=total,
            )
            order.save()
        request.session['cart']={}
        return redirect("/")
        
        
    
