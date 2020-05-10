from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.



class Category(models.Model):
    category_name=models.CharField(max_length=50)


    def __str__(self):
        return self.category_name



class Product(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.FloatField()
    product_image=models.ImageField()
    description=models.CharField(max_length=100)
    oldprice=models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)


    


class Coupon(models.Model):
    couponcode=models.CharField(max_length=5)
    coupon_price=models.CharField(max_length=50)



    def __str__(self):
        return self.coupon_price



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    orderproducts=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date=models.DateTimeField()         
    orderaddress=models.ForeignKey('BillingAddress',on_delete=models.SET_NULL,null=True,blank=True)
    orderstatus=models.BooleanField(default=False)



    def itemtotal(self):
        return self.quantity * self.orderproducts.price        

class BillingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    house_address=models.CharField(max_length=50)
    area_address=models.CharField(max_length=50)
    mobile_number=models.IntegerField()
    country=CountryField(blank_label="Select Country")
    zipcode=models.IntegerField()
    payment=models.CharField(max_length=10)



    def __str__(self):
        return self.house_address