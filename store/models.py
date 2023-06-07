from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

# CustomUserManager [slide-5 pag 12]

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a new user with the given username and password.
        """
        if not username:
            raise ValueError("The Username field must be set.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a new superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Category(models.Model):

    name = models.CharField(max_length=255)

class Product(models.Model):

    id = models.IntegerField(primary_key=True, unique=True, )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, primary_key=True, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

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

