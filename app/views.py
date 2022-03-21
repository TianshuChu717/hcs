from multiprocessing import context
# from ssl import _create_default_https_context
from django.contrib import auth
from django.contrib.auth.models import User
# from sklearn.metrics import classification_report

from app import models
from app.models import UserProfile, Goods, Likes
from django.shortcuts import render
from django.views.generic import View, ListView
import tkinter.messagebox
from tkinter import *

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse


# from django.contrib.auth import authenticate, login


def index(request):
    # return render(request, 'pages/index.html')
    good_content = {}
    if request.method == 'GET':
        try:
            goods = Goods.objects.all()
            good_content['goods'] = goods
        except Exception as e:
            good_content['goods'] = None
            print(str(e))
        if request.session.get('is_login', None):
            # if request.session["is_login"]:
            print("is login!")
            username = request.session["username"]
            try:
                user_pro = UserProfile.objects.get(username=username)
                liked_goods = Likes.objects.filter(likes_from=user_pro)
                good_content['liked_goods'] = liked_goods
            except Exception as e:
                good_content['liked_goods'] = None
                print(str(e))
        else:
            print("is not login!")
    print(good_content)
    return render(request, 'pages/index.html', context=good_content)


def register(request):
    if request.method == 'GET':
        return render(request, 'pages/registration.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('re_password')
        if password1 != password2:
            tkinter.messagebox.showinfo('Hint', 'The two passwords are not the same!')
            return render(request, 'pages/registration.html')
        else:
            same_name_user = UserProfile.objects.filter(username=name)
            if same_name_user:
                tkinter.messagebox.showinfo('Hint', 'The user name is occupied!')
                return render(request, 'pages/registration.html')
            same_email_user = UserProfile.objects.filter(email=email)
            if same_email_user:
                tkinter.messagebox.showinfo('Hint', 'The email address has been registered!')
                return render(request, 'pages/registration.html')
            if not User.objects.filter(username=name).exists():
                User.objects.create_user(username=name, password=password1)
            UserProfile.objects.create(username=name, password=password1, email=email)
            return render(request, 'pages/login.html')


def login(request):
    # if request.method == 'GET':
    #     return render(request, 'pages/login.html')
    context_dict = {}

    if request.method == 'POST':
        # print('1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        try:
            user = UserProfile.objects.get(username=username)
            if user.password == password:
                user.is_login = True
                user.save()
                request.session["is_login"] = "1"
                request.session["username"] = username
                return redirect("/")
            else:
                print("login error")
                context_dict['error'] = "Username or password is invalid."
                return render(request, 'pages/login.html', context=context_dict)
        except Exception as e:
            print(str(e))
    return render(request, 'pages/login.html')


def grid(request):
    content = {}
    username = request.GET.get('username')
    print(username)
    if request.method == 'GET':
        print('Generating grids')
        try:
            user_pro = UserProfile.objects.get(username=username)
            print("user is authenticated.")
            if user_pro:
                liked_goods = Likes.objects.filter(likes_from=user_pro).order_by('create_time').first()
                liked_good = liked_goods.likes_to
                goods = Goods.objects.all().order_by('?')[:8]
                content['goods'] = goods
                content['liked_goods'] = liked_good
                print("render")
                return render(request, 'pages/grids.html', context=content)
        except Exception as e:
            print(str(e))
    elif request.method == 'POST':
        username = request.POST.get('username')
        select_good_name = request.POST.get('good_name')
        try:
            user_pro = UserProfile.objects.get(username=username)
            liked_goods = Likes.objects.filter(likes_from=user_pro)
            select_good = Goods.objects.filter(name=select_good_name)
            if select_good in liked_goods:
                render(request, 'pages/login.html', context={'msg': 'success!'})
            else:
                render(request,'pages/login.html',content={'msg':'error!'})
        except Exception as e:
            print(str(e))

    return render(request, 'pages/grids.html', context=content)


def reset(request):
    context_dict = {}
    if request.method == 'GET':
        return render(request, 'pages/reset.html')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password1 = request.POST.get('new_password')
        password2 = request.POST.get('re_new_password')
        if User.objects.filter(username=username).exists():
            print(1)
            if password1 == password2:
                user = User.objects.get(username=username)
                user.set_password(password1)
                user.save()
                user_change = models.UserProfile.objects.get(username=username)
                user_change.password = password1
                user_change.save()
                return render(request, 'pages/login.html')
            else:
                context_dict['error'] = "The repeat new password is different."
                print("ERROR")
                return render(request, 'pages/reset.html', context=context_dict)
        else:
            print(2)
            return render(request, 'pages/reset.html')


def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'pages/login.html')


def add_like(request):
    # good_content = {}
    result = 0
    if request.method == 'POST':
        if not request.session.get('is_login', None):
            print("add_like: is not login!")
            render(request, "pages/login.html")
        username = request.session.get("username")
        good_name = request.POST['good']
        print(good_name)
        result = 2
        try:
            good = Goods.objects.get(name=good_name)
            user_pro = UserProfile.objects.get(username=username)
            Likes.objects.create(likes_from=user_pro, likes_to=good)
            good.likes_num = good.likes_num + 1
            good.number = good.number - 1
            good.save()
            print("done")
            result = 1
            #
            # liked_goods = Likes.objects.filter(likes_from=user_pro)
            # goods = Goods.objects.all()
            # good_content['goods'] = goods
            # good_content['liked_goods'] = liked_goods
        except Exception as e:
            # good_content['goods'] = None
            # good_content['liked_goods'] = None
            print(str(e))
    return HttpResponse(result)


def random_authentication(request):
    content = {}
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            user_pro = UserProfile.objects.get(username=username)
            if user_pro:
                liked_goods = Likes.objects.filter(likes_from=user_pro).order_by('?').first()
                liked_good = liked_goods.likes_to
                goods = Goods.objects.all().order_by('?')[:8]
                content['goods'] = goods
                content['liked_goods'] = liked_good
                return render(request, 'pages/login.html', context=content)
        except Exception as e:
            print(str(e))
    elif request.method == 'POST':
        username = request.POST.get('username')
        select_good_name = request.POST.get('good_name')
        try:
            user_pro = UserProfile.objects.get(username=username)
            liked_goods = Likes.objects.filter(likes_from=user_pro)
            select_good = Goods.objects.filter(name=select_good_name)
            if select_good in liked_goods:
                render(request, 'pages/login.html', context={'msg': 'success!'})
            else:
                render(request, 'pages/login.html', content={'msg': 'error!'})
        except Exception as e:
            print(str(e))
