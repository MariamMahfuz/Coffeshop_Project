from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    # path('Logout_attempt/', views.Logout_attempt, name='logout_attempt'),
    path('comment/', views.comment, name='comment'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('shop/', views.Shop, name='shop'),
    path('single_product/', views.Single_product, name='single_product'),
    path('contact/', views.Contact, name='contact'),
    path('blog/', views.Blog, name='blog'),
]
