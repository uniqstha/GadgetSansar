from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from django.contrib.auth import get_user_model
# Create your views here.

def login_signup(request):
    
    
    if (request.method=="POST"):
        if request.POST.get('submit') == 'sign_in': 
            fn=request.POST['fn']
            ln=request.POST['ln']
            un=request.POST['un']
            em=request.POST['em']
            ps=request.POST['ps']
            user=User.objects.create_user( first_name=fn, last_name=ln, username=un, email=em, password=ps)
            user.save()
            return redirect("/user/loginsignup")

        elif  request.POST.get('submit') == 'login':
            em=request.POST['em']
            ps=request.POST['ps']
            user=authenticate(request,username=em,password=ps)
            if user is not None:
                login(request, user)
                print("pass")
                return redirect("/")
            else:
                messages.error(request,'invalid')

            # 
    else:
        return render(request, 'loginSignup.html')

def logout_fn(request):
    logout(request)
    return redirect("/")
@login_required(login_url="/user/loginsignup")
def profile(request):
    # products = Products.objects.filter(productCategory='phone').values()
    # audio = Products.objects.filter(productCategory='audio').values()
    return render(request, 'profile.html' )