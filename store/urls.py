from django.urls import path
from .views import index


urlpatterns = [
    path("", index, name='home'),
    path("user/", index, name='user'),
    path("cart/<str:username>/", index, name='cart'),
    path("order/<str:username>/", index, name='order'),
    path("product/<int:id>", index, name='product'),
]

#TODO: change to correct urls (user, cart, order, product)

#TODO: add urls for each product (product/<int:id>/)

#TODO: index is the view function to call, change to correct view functions for each url (user, cart, order, product)
#each url, when matched with the request, should call the correct view function dinamically (usernames and product ids)