from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('rsubmit', views.rsubmit, name = 'rsubmit'),
    path('login', views.handelLogin, name='login'),
    path('logout', views.handelLogout, name='logout'),

]