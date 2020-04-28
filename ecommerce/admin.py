from django.contrib import admin
from .models import Product,Category,Cart,Coupon
# Register your models here.

admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Cart),
admin.site.register(Coupon)