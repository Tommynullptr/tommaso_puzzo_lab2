from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

# TODO: CustomUserManager? [slide-5 pag 12]


class Category(models.Model):

    name = models.CharField(max_length=255)

class Product(models.Model):

    id = models.IntegerField(primary_key=True, unique=True, )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class CustomUser(AbstractBaseUser, models.Model):

    username = models.CharField(max_length=255, primary_key=True, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    # should own a cart
    # cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)


class Cart(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


class Order(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

# TODO: alternative to manytomanyfield: add a field to the product model that is a list of users who have it in their cart and use a queryset

