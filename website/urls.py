"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce.views import home,productdetail,cart,signup,login,add_to_Cart,removeitem
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup),
    path('login/',login),
    path('home/',home.as_view()),
    path('productdetail/<pk>/',productdetail.as_view()),
    path('cart/',cart),
    path('addtocart/',add_to_Cart),
    path('removeitem/',removeitem)
] + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
