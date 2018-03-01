from django.shortcuts import render

from .models import Cart

def cart_home(request):
    # del request.session['cart_id']
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:  #and isinstance(cart_id, int):
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id
        print('new cart created')
    else:
        print('cart id exists')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
    # print(request.session)
    # key = request.session.session_key
    # print(key)
    request.session['first_name'] = 'Louis'
    return render(request, "carts/home.html", {})
