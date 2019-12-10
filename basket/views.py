from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from menu.models import Menu

@login_required(login_url='login')
def addCart(request, pk):
    foods = Menu.objects.get(pk=pk)
    try:
        cart = Product.objects.get(name=foods.name)
        cart.quantity+=1
        cart.price+=cart.price
        cart.save()
        return redirect("showcart")
    except:
        cart = Product(name=foods.name, image=foods.image, price= foods.price)
        cart.save()
        return redirect("showcart")


@login_required(login_url='login')
def showCart(request):
    total = 0
    cart = Product.objects.all()
    for cartt in cart:
        total += cartt.price
    return render(request, 'cart.html', {'carts':cart, 'total':total})

@login_required(login_url='login')
def delete(request, pk):
    try:
        Product.objects.get(pk=pk).delete()
        total = 0
        cart = Product.objects.all()
        for cartt in cart:
            total += cartt.price
        return render(request, 'cart.html', {'carts': cart, 'total': total})
    except:
        return redirect('showcart')