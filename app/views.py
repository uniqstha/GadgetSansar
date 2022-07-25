from django.http import JsonResponse
from django.shortcuts import render

from products.models import Product

# Create your views here.
def homepage(request):
    products = Product.objects.filter(productCategory='phone').values().order_by('-id')[0:4]
    audio = Product.objects.filter(productCategory='audio').values().order_by('-id')
    power = Product.objects.filter(productCategory='power').values().order_by('-id')
    fitness = Product.objects.filter(productCategory='fitness').values().order_by('-id')
    return render(request, 'homepage.html' ,{'products': products,'audio': audio,'power': power,'fitness': fitness, 'nbar':'home'})
    # return render(request,'homepage.html')



