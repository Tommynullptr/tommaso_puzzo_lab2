
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, Order, Category
from .forms import UserFormRegister, UserFormLogin



def home(request):

    return render(request, 'store/home.html')


def product_list(request):

    products = Product.objects.all()
    category_name = request.GET.get('category')

    if category_name:
        products = products.filter(category__name=category_name)

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'current_category': category_name if category_name else 'All Products',
    }

    return render(request, 'store/product_list.html', context)


def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


@login_required(login_url='login')
def add_to_cart(request, product_id):

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.listofproducts.add(product)
        cart.totalprice += product.price
        cart.save()
        return redirect('cart')

    else:
        return redirect('home')


@login_required(login_url='login')
def cart(request):

    cart = Cart.objects.get(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})


def remove_from_cart(request, product_id):

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart.listofproducts.remove(product)
        cart.totalprice -= product.price
        cart.save()
        return redirect('cart')


def checkout(request):

    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, totalprice=cart.totalprice)
        order.listofproducts.set(cart.listofproducts.all())
        cart.listofproducts.clear()
        cart.totalprice = 0
        cart.save()
        return redirect('order_confirmation')


def order_confirmation(request):

    return render(request, 'store/order_confirmation.html')

def register(request):

    if request.method == 'POST':
        form = UserFormRegister(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')

    else:
        form = UserFormRegister()

    return render(request, 'store/registration/register.html', {'form': form})

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

    return render(request, 'store/registration/login.html', {'form': form})

def user_logout(request):

    logout(request)
    return redirect('home')
