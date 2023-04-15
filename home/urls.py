from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]