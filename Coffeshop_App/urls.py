from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    # path('Logout_attempt/', views.Logout_attempt, name='logout_attempt'),
    path('comment/', views.comment, name='comment'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
