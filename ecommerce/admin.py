from django.contrib import admin
from .models import Product,Category,Cart,Coupon,Order,BillingAddress
# Register your models here.    

admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Cart),
admin.site.register(Coupon),
admin.site.register(Order),
admin.site.register(BillingAddress)