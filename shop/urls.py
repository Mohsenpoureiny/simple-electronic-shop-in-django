from django.urls import path
from shop.views import home

APP_NAME = "shop"

urlpatterns = [
    path('', home),
]
