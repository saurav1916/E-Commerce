from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import Product,Cart,Coupon,Order,BillingAddress
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
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
    paginate_by=1

    def get_context_data(self):
        context=super().get_context_data()
        if self.request.user.is_authenticated:
            context['cart_count']=Cart.objects.all().filter(user=self.request.user).count()
        return context


   
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
    return render(request,'cart.html',dict)


def add_to_Cart(request):
    product_id=request.GET['id']
    product=Product.objects.get(id=product_id)
    inc_quantity=1

    if request.method=="POST":
        inc_quantity=request.POST["quantity"]

    presentitem=Cart.objects.filter(user=request.user,products=product)
    if presentitem.exists():
        abc=presentitem[0]
        abc.quantity += int(inc_quantity)
        abc.save()
        messages.info(request," Item Quantity Is Updated")
    else:    
        Cart.objects.create(products=product,user=request.user,quantity=inc_quantity)
        messages.info(request,"Item Is Added to the cart")
    return HttpResponseRedirect('/home/')


def removeitem(request):
    id=request.GET['id']
    Cart.objects.all().filter(user=request.user,id=id).delete()
    return HttpResponseRedirect("/cart/")


def update_quantity(request):
    id=request.GET['id']
    if request.method=="POST":
        updated_quantity=request.POST['updatedquantity']

    if int(updated_quantity)==0:
        Cart.objects.all().filter(user=request.user,id=id).delete()
    else:    
        Cart.objects.all().filter(user=request.user,id=id).update(quantity=updated_quantity)
    return HttpResponseRedirect("/cart/")


def order(request):
    order_product_id=request.GET['id']
    order_product=Product.objects.get(id=order_product_id)
    order_date=timezone.now()
    order_quantity=request.GET['quantity']

    presentitem=Order.objects.all().filter(user=request.user,orderproducts=order_product,orderstatus=False)
    if presentitem.exists():
        abc=presentitem[0]
        abc.quantity += int(order_quantity)
        abc.save()
        Cart.objects.filter(user=request.user,products=order_product).delete()
    else:
        Order.objects.create(user=request.user,orderproducts=order_product,quantity=order_quantity,date=order_date)
        Cart.objects.filter(user=request.user,products=order_product).delete()
    return HttpResponseRedirect("/ordersummary/")


def ordersummary(request):
    orders=Order.objects.all().filter(user=request.user,orderstatus=False)
    cart_count=Cart.objects.all().filter(user=request.user).count()

    total=0
    for i in orders:
        total += i.itemtotal()
      
    context={"orders":orders,"total":total,
    "cart_count":cart_count}
    return render(request,"ordersummary.html",context)


def removeorder(request):
    id=request.GET['id']
    Order.objects.all().filter(user=request.user,id=id).delete()
    return HttpResponseRedirect("/ordersummary/")


def increase_order_quantity(request):
    order_id=request.GET['id']
    abc=Order.objects.get(id=order_id)
    abc.quantity += 1
    abc.save()
    messages.info(request,"Order Item Quantity increased")
    return HttpResponseRedirect("/ordersummary/")


def decrease_order_quantity(request):
    order_id=request.GET['id']
    abc=Order.objects.get(id=order_id)
    abc.quantity -= 1
    abc.save()
    messages.info(request,"Order Item Quantity Decreased")
    return HttpResponseRedirect("/ordersummary/")


def checkout(request):
    userorder= Order.objects.filter(user=request.user,orderstatus=False).all()
    if userorder.exists():
        form=CheckoutForm()
        if request.method=="POST":
            form=CheckoutForm(request.POST)
            if form.is_valid():
                print("hello1")
                obj=BillingAddress()
                obj.user=request.user
                obj.house_address=form.cleaned_data['house_address']
                obj.area_address=form.cleaned_data['area_address']
                obj.mobile_number=form.cleaned_data['mobile_number']
                obj.country=form.cleaned_data['country']
                obj.zipcode=form.cleaned_data['zipcode']
                obj.payment=form.cleaned_data['payment']
                obj.save()

                userorder= Order.objects.filter(user=request.user,orderstatus=False).all()
                for i in userorder:
                    i.orderaddress=obj
                    i.orderstatus=True
                    i.save()

                return HttpResponseRedirect('/placedorders/')

            else:
                print(form.errors)
        return render(request,"checkout.html",{"form":form})
        
    else:
        messages.info(request,"No Active Orders")
        return HttpResponseRedirect('/ordersummary/')    

         


def placedorders(request):
    orders_placed=Order.objects.all().filter(user=request.user,orderstatus=True)

    return render(request,'orders.html',{"ordersplaced":orders_placed})