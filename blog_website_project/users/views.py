from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from blog_app.models import Content


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('blog-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')


def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('updated-home-page')

def show_updated_home(request):
    context = {
        'data' : Content.objects.all()
    }
    return render(request, 'users/updated_home.html',context)

def show_logout(request):
    context = {}
    return render(request, 'users/logout.html',context)



