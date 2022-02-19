from django.shortcuts import render
from Coffeshop_App.models import Booking, Detail
from .models import *


# Create your views here.
def menu(request):
    if '1st_form' in request.POST:
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        text_date = request.POST.get('text_date')
        t_time = request.POST.get('t_time')
        phone_text = request.POST.get('phone_text')
        booking_message = request.POST.get('booking_message')

        appointment_ins = Booking(
            f_name=f_name,
            l_name=l_name,
            text_date=text_date,
            t_time=t_time,
            phone_text=phone_text,
            booking_message=booking_message
        )
        appointment_ins.save()
        return render(request, 'Coffeshop/index.html', context={})
    details = Detail.objects.all()
    starter = Starter.objects.all()
    maindish = mainDish.objects.all()
    dessert = Dessert.objects.all()
    drinks = Drinks.objects.all()
    dict = {'details': details,'starter':starter,'maindish':maindish,'dessert':dessert,'drinks':drinks}
    return render(request, 'Coffeshop/menu.html', context=dict)
