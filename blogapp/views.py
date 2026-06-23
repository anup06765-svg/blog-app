from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post   
from .import models
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
    return render(request,'blog/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')

    return render(request,'blog/signup.html')

def home(request):
    posts=Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})


def newpost(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.user

        Post.objects.create(
            title=title,
            content=content,
            author=author
        )

        return redirect('/home')
    return render(request,'blog/newpost.html')

def mypost(request):
    posts=Post.objects.filter(author=request.user)
    return render(request,'blog/mypost.html',{'posts':posts})


def signout(request):
    logout(request)
    return redirect('/login')