from django.shortcuts import redirect, render

from Menu_app.models import mainDish, Drinks, Dessert
from .models import *


def home(request):
    if request.method == 'POST':
        # print(request.POST)
        if '2nd_form' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date = request.POST.get('date')
            time = request.POST.get('time')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            booking_ins = Appointment_Booking(
                first_name=first_name,
                last_name=last_name,
                date=date,
                time=time,
                phone=phone,
                message=message
            )

            booking_ins.save()
            return redirect('/')

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
    discovering_story = Discover_story.objects.all()
    services = Service.objects.all()
    menu = Discover_menu.objects.all()
    best_products = Best_selling_product.objects.all()
    customer_says = Customer_saying.objects.all()
    blog = Blogs.objects.all()
    about_us = About_us.objects.all()
    our_services = Our_service.objects.all()
    maindish = mainDish.objects.all()
    dessert = Dessert.objects.all()
    drinks = Drinks.objects.all()

    dict = {'details': details, 'discovering_story': discovering_story, 'services': services, 'menu': menu,
            'best_products': best_products, 'maindish': maindish, 'customer_says': customer_says, 'blog': blog,
            'about_us': about_us, 'our_services': our_services, 'dessert': dessert, 'drinks': drinks}
    return render(request, 'Coffeshop/index.html', context=dict)


def comment(request):
    if request.method == 'POST':
        comment_body = request.POST.get('comment_body')
        date_added = request.POST.get('date_added')
        comment_ins = Comment(
            user=request.user,
            # person_name=person_name,
            comment_body=comment_body,
            date_added=date_added
        )
        comment_ins.save()
        return redirect('/comment/')
    comments = Comment.objects.all()
    dict = {'comments': comments}
    return render(request, 'Coffeshop/Comment.html', context=dict)


def Cart(request):
    cart_item = CartItem.objects.all()
    cart_subtotal = CartSubTotal.objects.all()
    dict = {'cart_item': cart_item,'cart_subtotal':cart_subtotal}
    return render(request, 'Coffeshop/cart.html', context=dict)

def checkout(request):
    dict={}
    return render(request,'Coffeshop/checkout.html',context=dict)