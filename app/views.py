from multiprocessing import context
from django.contrib import auth
from django.contrib.auth.models import User

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
                likes = Likes.objects.filter(likes_from=user_pro)
                likes_goods = []
                for like in likes:
                    good = like.likes_to
                    likes_goods.append(good)
                good_content['liked_goods'] = likes_goods

                not_liked = []
                for item in goods:
                    if item not in likes_goods:
                        not_liked.append(item)
                good_content['not_liked'] = not_liked
            except Exception as e:
                good_content['liked_goods'] = None
                print(str(e))
        else:
            print("is not login!")
    return render(request, 'pages/index.html', context=good_content)


# def register(request):
#     # if request.method == 'GET':
#     #     return render(request, 'pages/registration.html')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(username)
#         print(email)
#         print(password)
#
#         try:
#             user = UserProfile.objects.filter(username=username)
#             print(user)
#             if username not in user and username != '':
#                 UserProfile.objects.create(username=username, password=password, email=email)
#                 return render(request, 'pages/login.html')
#             else:
#                 HttpResponse("Your username is invalue")
#         except Exception as e:
#             print(str(e))
#     return render(request, 'pages/registration.html')

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
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
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
    request.session.flush()
    return HttpResponseRedirect('/app/login/')


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
                return render(request, 'pages/login.html', context={'msg': 'success!'})
            else:
                return HttpResponse("Wrong answer!")
        except Exception as e:
            print(str(e))
        return render(request, 'pages/login.html', context={'msg': 'Something wrong!'})


def comparison_authentication(request):
    content = {}
    if request.method == 'GET':
        print("GET!")
        return render(request, 'pages/comparison_authentication.html', context=content)
    elif request.method == 'POST':
        print("POST!")
        username = request.POST.get('user_name')
        print(username)
        good_name = request.POST.get('good_name')
        print(good_name)
        password = request.POST.get('new_password')
        print(password)
        re_password = request.POST.get('re_new_password')
        try:
            user_pro = UserProfile.objects.get(username=username)
            if not user_pro:
                return HttpResponse("This user does not exist!")
            liked_goods = Likes.objects.filter(likes_from=user_pro)
            liked_goods_name = []
            for liked_good in liked_goods:
                liked_goods_name.append(re.sub("[^a-zA-Z]", "", liked_good.likes_to.name))
            print(liked_goods_name)
            if good_name in liked_goods_name:
                if password == re_password:
                    user = User.objects.get(username=username)
                    user.set_password(password)
                    user.save()
                    user_change = UserProfile.objects.get(username=username)
                    user_change.password = password
                    user_change.save()
                    return render(request, 'pages/login.html', context={'msg': 'success!'})
                else:
                    HttpResponse("Please enter the same password twice!")
            else:
                return HttpResponse("Wrong answer!")
        except Exception as e:
            print(str(e))
        return render(request, 'pages/login.html', context={'msg': 'Something wrong!'})
