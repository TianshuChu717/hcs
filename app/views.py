from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View, ListView
import tkinter.messagebox
from tkinter import *

from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'pages/registration.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = auth.authenticate(username=username, password=password)
    #     print(user)
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect('/')
    #     else:
    #         tkinter.messagebox.showinfo('Hint', 'Incorrect password')
    #         return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/login/')
