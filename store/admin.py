from django.contrib import admin

from .models import CustomUser, Product, Category

# Register your models here.

admin.site.register(CustomUser, Product, Category)