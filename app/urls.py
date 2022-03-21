from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('grids/',views.grid,name="grids"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_like/', views.add_like, name='add_like'),
    path('reset/',views.reset,name="reset"),
]
