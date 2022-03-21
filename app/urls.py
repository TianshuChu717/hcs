from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_like/', views.add_like, name='add_like'),
    path('reset/',views.reset,name="reset"),
    path('compared_authentication/', views.comparison_authentication, name="compare_auth"),

]
