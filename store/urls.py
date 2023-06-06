#from django.urls import path
#from .views import index


#urlpatterns = [
 #   path("", index, name='home'),
  #  path("user/", index, name='user'),
   # path("cart/<str:username>/", index, name='cart'),
  #  path("order/<str:username>/", index, name='order'),
  #  path("product/<int:id>", index, name='product'),
#]

#TODO: change to correct urls (user, cart, order, product)

#TODO: add urls for each product (product/<int:id>/)

#TODO: index is the view function to call, change to correct view functions for each url (user, cart, order, product)
#each url, when matched with the request, should call the correct view function dinamically (usernames and product ids)

##############################################################################################



from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
