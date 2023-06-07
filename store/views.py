#from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpRequest
#from django.views import View
#from django.views.generic import FormView, ListView, DetailView

#from store.models import Cart, Order, Product
#from store.forms import UserFormRegister, UserFormLogin


# Create your views here.

#def index(request):

 #   return HttpResponse("Hello, world. You're at the store index.")


#class UserView(View): #TODO: make this view use the forms [check chatgpt (template loader configuration) + slide-4 pag 23,26 + slide-5 pag 22]

 #   template_name = 'user.html'

 #   def get(self, request):

 #       return HttpResponse("Hello, world. You're at the store user.")


#class CartView(ListView):

 #   model = Cart
 #   template_name = 'cart.html'

  #  def get_queryset(self):

   #     return Cart.objects.all().filter(user=self.request.user)


   # def get(self, request: HttpRequest, *args: str, **kwargs: str) -> HttpResponse:

    #    if not request.user.is_authenticated:
     #       return redirect("home")

      #  return HttpResponse("Hello, world. You're at your cart.") #return super().get(request, *args, **kwargs)


#class OrderView(ListView):

 #   model = Order
  #  template_name = 'order.html'

   # def get_queryset(self):

    #    return Order.objects.all().filter(user=self.request.user)


    #def get(self, request: HttpRequest, *args: str, **kwargs: str) -> HttpResponse:

     #   if not request.user.is_authenticated:
      #      return redirect("home")

       # return HttpResponse("Hello, world. You're at your order.") #return super().get(request, *args, **kwargs)


#class ProductView(DetailView):

 #   model = Product
  #  template_name = 'product.html'

   # def get(self, request):

    #    return HttpResponse("Hello, world. You're at the store product.")

    #def get(self, request, *args, **kwargs):
        # Call the parent class's get() method to trigger the template rendering process
        #return super().get(request, *args, **kwargs)



#TODO: create cart and order CreateView? [slide-4 pag 5]

##############################################################################################################


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .models import Product, Cart, Order, Category
from .forms import UserFormRegister, UserFormLogin


# Home View
def home(request):

    return render(request, 'home.html')

# Product Listing View
def product_list(request):

    products = Product.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        'products': products,
        'categories': Category.objects.all(),
    }

    return render(request, 'product_list.html', context)

# Product Detail View
def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Add Item to Cart View
def add_to_cart(request, product_id):

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.listofproducts.add(product)
        cart.totalprice += product.price
        cart.save()
        return redirect('cart')

# Cart View
def cart(request):

    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

# Remove Item from Cart View
def remove_from_cart(request, product_id):

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart.listofproducts.remove(product)
        cart.totalprice -= product.price
        cart.save()
        return redirect('cart')

# Checkout View
def checkout(request):

    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, totalprice=cart.totalprice)
        order.listofproducts.set(cart.listofproducts.all())
        cart.listofproducts.clear()
        cart.totalprice = 0
        cart.save()
        return redirect('order_confirmation')

# Order Confirmation View
def order_confirmation(request):

    return render(request, 'order_confirmation.html')

def register(request):

    if request.method == 'POST':
        form = UserFormRegister(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')

    else:
        form = UserFormRegister()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):

    if request.method == 'POST':
        form = UserFormLogin(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('product_list')

            else:
                form.add_error(None, 'Invalid username or password.')

    else:
        form = UserFormLogin()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):

    logout(request)
    return redirect('product_list')

#TODO: However, please note that the add_to_cart and remove_from_cart views are only accessible for authenticated users. You may want to consider adding authentication checks and handling scenarios where a user is not authenticated.
