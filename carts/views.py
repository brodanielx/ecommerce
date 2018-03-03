from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})

def cart_update(request):
    prodcut_id = 1
    product_obj = Product.objects.get(id=prodcut_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(product_obj)
    return redirect("cart:home")
