import random
import string
import uuid
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .helpers import send_forget_password_mail
from .models import *
from Coffeshop_App.views import home

# def generate_
# _id():
#     s = 6
#     global student_id
#     student_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
#     student_id = "#MZ" + str(student_id)
#     return student_id


#Create your views here.
# def index(request):
#     dict = {}
#     return render(request, 'Coffeshop/index.html', context=dict)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login_user/')
        profile_obj = Profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login_user/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login_user/')

        login(request, user)
        return redirect('/')

    dict = {}
    return render(request, 'User_Authentication/Login.html', context=dict)


def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
                messages.success(request, "Username is already taken")
                return redirect('/Register_user/')
            if User.objects.filter(email=email).first():
                messages.success(request, "email is already taken")
                return redirect('/Register_user/')
            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)


        except Exception as e:
            print(e)
    dict = {}
    return render(request, 'User_Authentication/Register.html', context=dict)


def Success(request):
    dict = {}
    return render(request, 'User_Authentication/Success.html', context=dict)


def token_send(request):
    dict = {}
    return render(request, 'User_Authentication/Token_send.html', context=dict)


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Please verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def error_page(request):
    dict = {}
    return render(request, 'User_Authentication/Error.html', context=dict)


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, "your account has already varified")
                return redirect('/login_user/')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "Your account has been varified")
            return redirect('/login_user/')
        else:
            return redirect('/Error/')
    except Exception as e:
        print(e)
        return redirect('/')

    dict = {}
    return render(request, 'User_Authentication/Token_send.html', context=dict)


def forget_password(request):
    dict = {}
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(User, "User not found")
                return redirect('/forget_password/')

            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget_password/')

    except Exception as e:
        print(e)
    return render(request, 'User_Authentication/forget_password.html', context=dict)


def change_password(request, token):
    try:
        profile_obj = Profile.objects.filter(forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'both did not match.')
                return redirect(f'/change-password/{token}/')

            user_obj = User.objects.get(id=user_id)

            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, "Password Has Been Changed!")

            return redirect('/login_user/')
    except Exception as e:
        print(e)
        dict = {}

    return render(request, 'User_Authentication/change_pass.html', context)

def Logout_attempt(request):
    logout(request)
    return redirect('/')

