from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import Product,Cart
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
        


class home(ListView):
    model=Product
    template_name='home.html'

class productdetail(DetailView):
    model=Product
    template_name='product.html'


def cart(request):
    cart=Cart.objects.all().filter(user=request.user)
    count=Cart.objects.all().filter(user=request.user).count()
    
    total=0
    for i in cart:
        t=i.products.price
        total=int(t)+int(total)
    dict={"cart":cart,"total":total,"count":count}      
    return render(request,'checkout.html',dict)
    
def add_to_Cart(request):
    id=request.GET['id']
    products=Product.objects.get(id=id)
    Cart.objects.get_or_create(products=products,user=request.user,quantity=1)
    return HttpResponseRedirect('/cart/')


def removeitem(request):
    id=request.GET['id']
    Cart.objects.all().filter(user=request.user,id=id).delete()
    return HttpResponseRedirect("/cart/")
