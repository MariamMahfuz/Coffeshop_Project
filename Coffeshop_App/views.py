from django.shortcuts import redirect, render
from Menu_app.models import mainDish, Drinks, Dessert
from .models import *
from django.core.paginator import Paginator


def home(request):
    if request.method == 'POST':
        if 'add_to_cart' in request.POST:
            product = Best_selling_product.objects.get(pk=request.POST.get('id'))
            print(product)
            temp_cart_ins = Temp_cart(user=request.user, product_id=product)
            print(temp_cart_ins)
            temp_cart_ins.save()
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
    # cart_item = CartItem.objects.all()
    cart_subtotal = CartSubTotal.objects.all()
    temp_cart = Temp_cart.objects.filter(user=request.user)
    our_services = Our_service.objects.all()
    extra_charges = CartSubTotal.objects.all()
    details = Detail.objects.all()
    delivery = 0
    discount = 0
    total = 0
    for item in extra_charges:
        delivery += item.delivery
        discount += item.discount
    for item in temp_cart:
        total += item.product_id.product_price
    dict = {'details': details,'cart_subtotal': cart_subtotal, 'temp_cart': temp_cart, 'delivery': delivery, 'discount': discount,
            'total': total, 'subtotal': total + delivery + discount,'our_services': our_services}
    return render(request, 'Coffeshop/cart.html', context=dict)


def checkout(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        state = request.POST.get('state')
        street = request.POST.get('street')
        apartment = request.POST.get('apartment')
        town = request.POST.get('town')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        direct_bank_payment = request.POST.get('direct_bank_payment')
        cash_on_delivery = request.POST.get('cash_on_delivery')
        paypal_payment = request.POST.get('paypal_payment')
        billing_details = Billing_Details(
            firstname=firstname,
            lastname=lastname,
            state=state,
            street=street,
            apartment=apartment,
            town=town,
            postcode=postcode,
            phone=phone,
            email=email,
            direct_bank_payment=direct_bank_payment,
            cash_on_delivery=cash_on_delivery,
            paypal_payment=paypal_payment
        )

        billing_details.save()
        # print(direct_bank_payment)

    cart_subtotal = CartSubTotal.objects.all()
    temp_cart = Temp_cart.objects.filter(user=request.user)
    extra_charges = CartSubTotal.objects.all()
    our_services = Our_service.objects.all()
    area = state_area.objects.all()
    details = Detail.objects.all()
    delivery = 0
    discount = 0
    total = 0
    for item in extra_charges:
        delivery += item.delivery
        discount += item.discount
    for item in temp_cart:
        total += item.product_id.product_price
    dict = {'details': details,'cart_subtotal': cart_subtotal, 'temp_cart': temp_cart, 'delivery': delivery, 'discount': discount,
            'total': total, 'subtotal': total + delivery + discount, 'area': area,'our_services': our_services}
    return render(request, 'Coffeshop/checkout.html', context=dict)


def service(request):
    services = Service.objects.all()
    our_services = Our_service.objects.all()
    details = Detail.objects.all()
    dict = {'services': services,'our_services': our_services}
    return render(request, 'Coffeshop/services.html', context=dict)
def about(request):
    discovering_story = Discover_story.objects.all()
    customer_says = Customer_saying.objects.all()
    menu = Discover_menu.objects.all()
    our_services = Our_service.objects.all()
    details = Detail.objects.all()
    dict={'details': details,'discovering_story':discovering_story,'customer_says':customer_says,'menu':menu,'our_services': our_services}
    return render(request,'Coffeshop/about.html',context=dict)

def Shop(request):
    maindish = mainDish.objects.all()
    dessert = Dessert.objects.all()
    drinks = Drinks.objects.all()
    our_services = Our_service.objects.all()
    details = Detail.objects.all()
    dict={'details': details,'maindish':maindish,'dessert': dessert, 'drinks': drinks,'our_services': our_services}
    return render(request,'Coffeshop/shop.html',context=dict)

def Single_product(request):
    product_detail=Product_Detail.objects.all()
    maindish = mainDish.objects.all()
    dessert = Dessert.objects.all()
    drinks = Drinks.objects.all()
    our_services = Our_service.objects.all()
    details = Detail.objects.all()
    dict = {'details': details,'product_detail':product_detail,'maindish': maindish, 'dessert': dessert, 'drinks': drinks,'our_services': our_services}
    return render(request, 'Coffeshop/product-single.html', context=dict)

def Contact(request):
    contact_info=Contact_info.objects.all()
    mail= Mail.objects.all()
    details = Detail.objects.all()
    our_services = Our_service.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email_address = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Mail_ins=Mail(
            name=name,
            email_address=email_address,
            subject=subject,
            message=message
        )
        Mail_ins.save()

    dict={'details': details,'contact_info':contact_info,'mail':mail,'our_services': our_services}
    return render(request,'Coffeshop/contact.html',context=dict)

def Blog(request):
    blog = Blogs.objects.all().order_by('id')
    details = Detail.objects.all()
    our_services = Our_service.objects.all()
    paginator=Paginator(blog,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page((page_number))
    dict={'page_obj':page_obj,'details': details,'blog':blog,'our_services': our_services}
    return render(request,'Coffeshop/blog.html',context=dict)