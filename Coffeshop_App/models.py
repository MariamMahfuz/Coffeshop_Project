from django.db import models

from User_Authentication_App.models import User, Profile


# Create your models here.
class Booking(models.Model):
    f_name = models.CharField(blank=True, null=True, max_length=30)
    l_name = models.CharField(blank=True, null=True, max_length=30)
    text_date = models.CharField(blank=True, null=True, max_length=20)
    t_time = models.CharField(blank=True, null=True, max_length=20)
    phone_text = models.CharField(blank=True, null=True, max_length=12)
    booking_message = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return str(self.f_name)


class Appointment_Booking(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    date = models.CharField(blank=True, null=True, max_length=20)
    time = models.TimeField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=12)
    message = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return str(self.first_name)


class Detail(models.Model):
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    address = models.CharField(blank=True, null=True, max_length=15)
    address_details = models.CharField(blank=True, null=True, max_length=50)
    opening_date = models.CharField(blank=True, null=True, max_length=20)
    opening_hours = models.CharField(blank=True, null=True, max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.address)


class Discover_story(models.Model):
    story = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.story)


class Service(models.Model):
    service1_heading = models.CharField(max_length=20, null=True, blank=True)
    service1_description = models.CharField(max_length=100, null=True, blank=True)
    service2_heading = models.CharField(max_length=20, null=True, blank=True)
    service2_description = models.CharField(max_length=100, null=True, blank=True)
    service3_heading = models.CharField(max_length=20, null=True, blank=True)
    service3_description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.service1_heading)


class Discover_menu(models.Model):
    menu_detail = models.CharField(max_length=300, null=True, blank=True)
    menu1 = models.ImageField(upload_to='media')
    menu2 = models.ImageField(upload_to='media')
    menu3 = models.ImageField(upload_to='media')
    menu4 = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.menu_detail)


class Best_selling_product(models.Model):
    product_photo = models.ImageField(upload_to='media')
    product_name = models.CharField(blank=True, null=True, max_length=30)
    product_details = models.CharField(blank=True, null=True, max_length=150)
    product_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.product_name)


class Customer_saying(models.Model):
    quote = models.CharField(max_length=500, blank=False, null=False)
    customer_name = models.CharField(max_length=30, blank=False, null=False)
    customer_profession = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.customer_name)


class Blogs(models.Model):
    blog_image = models.ImageField(upload_to='media')
    date = models.CharField(max_length=10)
    writer = models.CharField(max_length=15)
    blog_heading = models.CharField(max_length=30)
    blog_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.blog_heading)


class About_us(models.Model):
    about = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return str(self.about)


class Our_service(models.Model):
    service = models.CharField(max_length=70, blank=False, null=False)

    def __str__(self):
        return str(self.service)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment_body = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=1)
    total = models.FloatField(default=0)
    item_name = models.CharField(max_length=30, blank=True, null=True)
    Item_description = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.item_name)
class CartSubTotal(models.Model):
    subtotal=models.FloatField(default=0)
    delivery=models.FloatField(default=0)
    discount=models.FloatField(default=0)
    Total=models.FloatField(default=0)

    def __str__(self):
        return str(self.Total)

class Billing_Details(models.Model):
    firstname=models.CharField(max_length=50,null=False,blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    state=models.CharField(max_length=30)
    street=models.CharField(max_length=50,null=False,blank=False)
    apartment = models.CharField(max_length=200, null=False, blank=False)
    town=models.CharField(max_length=50,null=False,blank=False)
    postcode = models.CharField(max_length=50, null=False, blank=False)
    phone=models.CharField(max_length=13,blank=False,null=False)
    email=models.EmailField(null=False,blank=True)
