from django.db import models

from User_Authentication_App.models import User, Profile


# Create your models here.
class Starter(models.Model):
    starter_dish_image = models.ImageField(upload_to='media')
    starter_name = models.CharField(max_length=30, null=True, blank=True)
    starter_descripion = models.CharField(max_length=300, null=True, blank=True)
    starter_price = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.starter_name)

class mainDish(models.Model):
    main_dish_image = models.ImageField(upload_to='media')
    main_dish_name = models.CharField(max_length=30, null=True, blank=True)
    main_dish_description = models.CharField(max_length=300, null=True, blank=True)
    main_dish_price = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.main_dish_name)

class Dessert(models.Model):
    dessert_image = models.ImageField(upload_to='media')
    dessert_name = models.CharField(max_length=30, null=True, blank=True)
    dessert_descrtipion = models.CharField(max_length=300, null=True, blank=True)
    dessert_price = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.dessert_name)
class Drinks(models.Model):
    drinks_image = models.ImageField(upload_to='media')
    drinks_name = models.CharField(max_length=30, null=True, blank=True)
    drinks_descrtipion = models.CharField(max_length=300, null=True, blank=True)
    drinks_price = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.drinks_name)