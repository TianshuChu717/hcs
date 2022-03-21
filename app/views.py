from django.contrib import auth
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
    # if request.method == 'GET':
    #     return render(request, 'pages/registration.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(email)
        print(password)

        try:
            user = UserProfile.objects.filter(username=username)
            print(user)
            if username not in user and username != '':
                UserProfile.objects.create(username=username, password=password, email=email)
                return render(request, 'pages/login.html')
            else:
                HttpResponse("Your username is invalue")
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
                HttpResponse("Incorrect username or password")
        except Exception as e:
            print(str(e))
    return render(request, 'pages/login.html')


# def register(request):
#     registered = False
#     if request.method == 'POST':
#         # username = request.POST.get('name')
#         # password = request.POST.get('password')
#         # email = request.POST.get('email')
#         # money = 100
#         user_form = UserForm(request.POST)
#         profile_form = UserProfileForm()
#         # user_form = UserForm()
#         # profile_form = UserProfileForm()
#         # user_form.username = username
#         # user_form.password = password
#         # user_form.email = email
#         # profile_form.money = money
#
#         if user_form.is_valid():
#             print('1')
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.money = 1000
#             profile.save()
#             registered = True
#             redirect("/login/")
#         else:
#             print("2")
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#     return render(request, 'pages/registration.html',
#                   context={'user_form': user_form,
#                            'profile_form': profile_form,
#                            'registered': registered})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect("/")
#             else:
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#             print(f"Invalid login details: {username}, {password}")
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/login/')

#
# def show_all_goods(request):
#     good_content = {}
#     if request.method == 'GET':
#         username = request.GET.get('name')
#         try:
#             user_pro = UserProfile.objects.get(username=username)
#             liked_goods = Likes.objects.filter(likes_from=user_pro)
#             # goods = Goods.objects.filter(likes__likes_from=user_pro)
#             goods = Goods.objects.all()
#             good_content['goods'] = goods
#             good_content['liked_goods'] = liked_goods
#         except Exception as e:
#             good_content['goods'] = None
#             good_content['liked_goods'] = None
#             print(str(e))
#     print(good_content)
#     return render(request, 'pages/index.html', context=good_content)


def add_like(request):
    # good_content = {}
    if request.method == 'POST':
        if not request.session.get('is_login', None):
            print("add_like: is not login!")
            render(request, "pages/login.html")
        username = request.session["username"]
        good_name = request.POST.get('good_name')
        try:
            good = Goods.objects.get(name=good_name)
            user_pro = UserProfile.objects.get(username=username)
            Likes.objects.create(likes_from=user_pro, likes_to=good)
            likes_num = good.likes_num + 1
            number = good.number - 1
            Goods.objects.update(name=good_name, likes_num=likes_num, number=number)
            #
            # liked_goods = Likes.objects.filter(likes_from=user_pro)
            # goods = Goods.objects.all()
            # good_content['goods'] = goods
            # good_content['liked_goods'] = liked_goods
        except Exception as e:
            # good_content['goods'] = None
            # good_content['liked_goods'] = None
            print(str(e))
    return redirect("/")


# def forget_password(request):
#     content = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         new_password = request.POST.get('new_password')
#         try:
#             user_pro = UserProfile.objects.get(username=username)
#             if user_pro:
#                 content['username'] = username
#                 content['new_password'] = new_password
#                 return render(request, 'pages/check.html', context=content)
#             else:
#                 HttpResponse("This user does not exist.")
#         except Exception as e:
#             print(str(e))
#     return render(request, 'pages/forget_password.html')


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
                HttpResponse("Wrong answer!")
        except Exception as e:
            print(str(e))