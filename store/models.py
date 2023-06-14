
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User


# Create your models here.

# CustomUserManager [slide-5 pag 12]

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):

        if not username:
            raise ValueError("The Username field must be set.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Category(models.Model):

    name = models.CharField(max_length=255, primary_key=True, unique=True)

class Product(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, null=True)


class Cart(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField(null=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Order(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#alternative to manytomanyfield: add a field to the product model that is a list of users who have it in their cart and use a queryset

