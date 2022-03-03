from django.urls import path
from shop.views import *

APP_NAME = "shop"

urlpatterns = [
    path('', home),
    path('basket/', basket),
    path('product/', get_single_product_detail),
    path('product/<int:id>/', product_detail),
    path('order/', makeOrder),
    path('shop-status/<str:id>', shop_status),
]
