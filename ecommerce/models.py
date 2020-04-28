from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    category_name=models.CharField(max_length=50)


    def __str__(self):
        return self.category_name



class Product(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.CharField(max_length=20)
    product_image=models.ImageField()
    description=models.CharField(max_length=100)
    oldprice=models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=20,default=0)


    


class Coupon(models.Model):
    couponcode=models.CharField(max_length=5)
    coupon_price=models.CharField(max_length=50)



    def __str__(self):
        return self.coupon_price