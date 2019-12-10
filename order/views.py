from django.shortcuts import render
from menu.models import Menu
from basket.models import Product

def payCart(request):
    total = 0
    cart = Product.objects.all()
    for cartt in cart:
        total += cartt.price

    return render(request, 'cartorder.html', {'price':total})


def pay(request, pk):
    price = Menu.objects.get(pk=pk)
    return render(request, 'payment.html', {'price':price})
