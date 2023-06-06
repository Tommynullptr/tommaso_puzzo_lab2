from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from store.models import Cart, Order, Product
from store.forms import UserFormRegister, UserFormLogin


# Create your views here.

def index(request):

    return HttpResponse("Hello, world. You're at the store index.")


class UserView(View): #TODO: make this view use the forms [check chatgpt (template loader configuration) + slide-4 pag 23,26 + slide-5 pag 22]

    template_name = 'user.html'

    def get(self, request):

        return HttpResponse("Hello, world. You're at the store user.")


class CartView(ListView):

    model = Cart
    template_name = 'cart.html'

    def get_queryset(self):

        return Cart.objects.all().filter(user=self.request.user)


    def get(self, request: HttpRequest, *args: str, **kwargs: str) -> HttpResponse:

        if not request.user.is_authenticated:
            return redirect("home")

        return HttpResponse("Hello, world. You're at your cart.") #return super().get(request, *args, **kwargs)


class OrderView(ListView):

    model = Order
    template_name = 'order.html'

    def get_queryset(self):

        return Order.objects.all().filter(user=self.request.user)


    def get(self, request: HttpRequest, *args: str, **kwargs: str) -> HttpResponse:

        if not request.user.is_authenticated:
            return redirect("home")

        return HttpResponse("Hello, world. You're at your order.") #return super().get(request, *args, **kwargs)


class ProductView(DetailView):

    model = Product
    template_name = 'product.html'

    def get(self, request):

        return HttpResponse("Hello, world. You're at the store product.")

    #def get(self, request, *args, **kwargs):
        # Call the parent class's get() method to trigger the template rendering process
        #return super().get(request, *args, **kwargs)



#TODO: create cart and order CreateView? [slide-4 pag 5]