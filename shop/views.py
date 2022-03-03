import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *


def home(request):
    return HttpResponse("Hi")


@csrf_exempt
def makeOrder(request):
    try:
        if (request.method != "POST"):
            return HttpResponseNotFound("bad method of request")
        print(request.body)
        data = json.loads(request.body)
        customerInfo = data["customer"]
        customer = Customer(
            name=customerInfo["name"],
            last_name=customerInfo["last_name"],
            passport_id=customerInfo["passport_id"],
            phone_number=customerInfo["phone_number"],
            address=customerInfo["address"],
            post_code=customerInfo["post_code"],
        )
        customer.save()
        order = Order(customer=customer)
        order.save()
        for prodoctInfo in data["products"]:
            product = Product.objects.filter(id=int(prodoctInfo["id"])).first()
            countOfOrder = int(prodoctInfo["count"])
            if product.count < countOfOrder:
                return HttpResponseBadRequest(f"not enough count of {product.name}")
            product.count -= countOfOrder
            order_row = OrderRow(
                order=order, count=countOfOrder, product=product)
            order_row.save()
            product.save()
        order.status = "DOING"
        order.save()
        return HttpResponse(f"{order.tracking_code}")
    except Exception as e:
        return HttpResponseBadRequest("bad request" + str(e))

# example of body:
#    {
#        "customer":{
#            "name": "Name" ,
#            "last_name": "last name",
#            "passport_id": "15438512",
#            "phone_number": "+98451235435",
#            "address": "address" ,
#            "post_code": 425364758
#        },
#        "products":[
#            {
#                "id" : 1,
#                "count" : 1
#            }
#        ]
#    }
