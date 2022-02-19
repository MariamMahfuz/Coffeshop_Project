from django.urls import path
from Coffeshop_App.models import User,Booking,Detail
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),

]
