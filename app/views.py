from django.contrib import auth
from app.models import UserProfile
from django.shortcuts import render
from django.views.generic import View, ListView
import tkinter.messagebox
from tkinter import *

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from app.forms import UserForm
from django.views.generic import View
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def register(request):
    # if request.method == 'GET':
    #     return render(request, 'pages/registration.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        # print(name)
        email = request.POST.get('email')
        # print(email)
        password = request.POST.get('password')
        # print(password)

        try:
            user1 = UserProfile.objects.create(name=name, password=password, email=email)
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
                return render(request, 'pages/registration.html')
            else:
                HttpResponse("Incorrect password")
        except Exception as e:
            print(str(e))
    return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/login/')
