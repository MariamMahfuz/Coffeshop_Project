from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('Register_user/', views.register_user, name='register_user'),
    path('Success/', views.Success, name='success'),
    path('Token_send/', views.token_send, name='token_send'),
    path('Error/', views.error_page, name='error_page'),
    path('verify/<auth_token>/', views.verify, name='verify'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('change_pass/<token>/', views.change_password, name='change_password'),
    path('Logout_attempt/', views.Logout_attempt, name='logout_attempt'),

]
