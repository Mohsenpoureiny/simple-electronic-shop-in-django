from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    parent_id = models.ForeignKey(
        'Category', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='Provider')
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    short_description = models.TextField()
    product_picture = models.ImageField(upload_to='Product')
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tag')
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    creation_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    passport_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    post_code = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.last_name} {self.passport_id}"


class Order(models.Model):
    tracking_code = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)
    status_list = [
        ("INITIATED", "شروع شده"),
        ("PAYMENT_SUCCESSFULL", "payment successfull"),
        ("PAYMENT_FAILS", "payment fails"),
        ("DOING", "در حال ارسال مرسوله"),
        ("COMPLETED", " تحویل داده شده"),
    ]
    status = models.CharField(
        max_length=200, choices=status_list, default="INITIATED")
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.customer.name} {self.id}"


class OrderRow(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.order} {self.product} {self.count}"
