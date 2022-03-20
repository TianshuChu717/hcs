from multiprocessing import context
from ssl import _create_default_https_context
from django.contrib import auth
from app.models import UserProfile
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View, ListView
import tkinter.messagebox
from tkinter import *

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from app.models import Goods,UserProfile,Likes,User

#Display Groceries
def index(request):
    context_dict = {}
    try:
        u_name = request.COOKIE.get('username')
        user =  UserProfile.objects.get(name=u_name) 
        likes = Likes.objects.filter(like_from=user)
        context_dict['like_goods'] = []
        for like in likes:
            good = Goods.objects.filter(good=like.like_to)
            context_dict['like_goods'].append(good)
        goods = Goods.objects.all()
        context_dict['goods'] = goods
    except Exception as e:
        goods = Goods.objects.all()
        context_dict['goods'] = goods
        context_dict['like_goods'] = None
    return render(request, 'pages/index.html',context = context_dict)

#Update like table
def like_good(request,good_name):
    try:
        u_name = request.COOKIE.get('username')
        user = UserProfile.objects.get(name=u_name) 
        good = Goods.objects.filter(name = good_name)
        #How to update sql in sqlite

        return redirect(reverse('app:index'))
    except Exception as e:
        print("add like fail.")

def register(request):
    # if request.method == 'GET':
    #     return render(request, 'pages/registration.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user = UserProfile.objects.create(name=name, password=password, email=email)
            user.save()

            return render(request, 'pages/login.html')
        except Exception as e:
            print(str(e))
    return render(request, 'pages/registration.html')

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'pages/login.html')
    if request.method == 'POST':
        # print('1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # print(username)
        # print(password)
        try:
            user = UserProfile.objects.get(name=username)
            if user.password == password:
                return redirect(reverse('app:index'))
            else:
                HttpResponse("Incorrect password")
        except Exception as e:
            print(str(e))
    return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/login/')
