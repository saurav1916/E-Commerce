from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import Product,Cart,Coupon
# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        return HttpResponseRedirect('/login')
    return render(request,"signup.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect("/home/")
        else:
            return redirect('/wrong.html')
    return render(request,"login.html")
        

def logout(request):
    auth_logout(request)
    return redirect('/login')


class home(ListView):
    model=Product
    template_name='home.html'

   



class productdetail(DetailView):
    model=Product
    template_name='product.html'


def cart(request):
    cart=Cart.objects.all().filter(user=request.user)
    count=Cart.objects.all().filter(user=request.user).count()

    discount=0
    promocode=""
    if request.method=="POST":
        promocode=request.POST['promocode']
        discount_coupon=Coupon.objects.get(couponcode=promocode)
        discount=discount_coupon.coupon_price
        
    
    total=0
    for i in cart:
        quantity=i.quantity
        t=i.products.price
        total=(int(t)*int(quantity))+int(total)
    total=int(total)-int(discount)

    dict={"cart":cart,"total":total,"count":count,"discount":discount,"promocode":promocode}      
    return render(request,'checkout.html',dict)


def add_to_Cart(request):
    id=request.GET['id']
    inc_quantity=1

    if request.method=="POST":
        inc_quantity=request.POST["quantity"]

    products=Product.objects.get(id=id)
    presentitem=Cart.objects.filter(user=request.user,products=products)
    if presentitem.exists():
        abc=presentitem[0]
        abc.quantity += int(inc_quantity)
        abc.save()
    else:    
        Cart.objects.create(products=products,user=request.user,quantity=inc_quantity)
    return HttpResponseRedirect('/cart/')


def removeitem(request):
    id=request.GET['id']
    Cart.objects.all().filter(user=request.user,id=id).delete()
    return HttpResponseRedirect("/cart/")


