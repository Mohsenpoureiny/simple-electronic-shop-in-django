from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderRow)
