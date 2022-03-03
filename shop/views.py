import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.forms.models import model_to_dict


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {
        "products": products,
        "categories": categories
    })


def basket(request):
    categories = Category.objects.all()

    return render(request, "basket.html", {
        "categories": categories
    })


def shop_status(request, id):
    try:
        categories = Category.objects.all()
        order = Order.objects.filter(tracking_code=id).first()
        return render(request, "shop-status.html", {
            "level": order.get_status_display(),
            "status": True,
            "categories": categories
        })
    except:
        return render(request, "shop-status.html", {
            "status": False
        })


def product_detail(request, id):
    product = Product.objects.filter(id=int(id)).first()
    tags = product.tag.all()
    categories = Category.objects.all()
    return render(request, "single-product.html", {
        "product": product,
        "tags": tags,
        "categories": categories
    })


def get_single_product_detail(request):
    product = Product.objects.filter(
        id=int(request.GET["id"])).first().__dict__
    print(product)
    # product["product_picture"] = str(product["product_picture"])
    return JsonResponse({
        "name": product["name"],
        "short_description": product["short_description"],
        "product_picture": str(product["product_picture"]),
        "count": product["count"],
        "price": product["price"],
        "id": product["id"],
    })


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
