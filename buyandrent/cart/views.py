from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import House
from .cart import Cart
from .forms import CartAddHouseForm

@require_POST
def cart_add(request, house_id):
    cart = Cart(request)
    house = get_object_or_404(House, id=house_id)
    form = CartAddHouseForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(house=house,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, house_id):
    cart = Cart(request)
    house = get_object_or_404(House, id=house_id)
    cart.remove(house)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddHouseForm(
                          initial={'quantity': item['quantity'],
                          'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})