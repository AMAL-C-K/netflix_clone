from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login
import re

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
        elif password != confirm_password:
            messages.error(request, 'password not matching')
        elif not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', password):
            messages.error(request, 'password contains atleast one (0-9),(a-z),(A-Z) special characters ')
        else:
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password)    
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')   
    return render(request, 'login.html')

def signout(request):
    auth.logout(request)
    return redirect('/')