from django.urls import path
from shop.views import *

APP_NAME = "shop"

urlpatterns = [
    path('', home),
    path('order/', makeOrder),
]
