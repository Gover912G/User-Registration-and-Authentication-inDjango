from django.shortcuts import render,redirect
from .forms import Userform,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def home(request):

    return render(request, 'users/index.html')

def register_user(request):
    form = Userform
    if request.method == 'POST':
        form=Userform(request.POST)
        if form.is_valid:
            form.save()

            return redirect('login')
    context = {
        "form":form
    }
    return render(request, 'users/register.html', context)


def login_user(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid:
            username = request.POST.get('username')
            password  = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {
        "form":form
    }

    return render(request, 'users/login.html', context)
    

def dashboard(request):
    return render(request, 'users/dashboard.html')
    

def logout_user(request):
    auth.logout(request)

    return redirect('home')