from django.shortcuts import render
from .models import Menu



def menu(request):
    products = Menu.objects.all()

    return render(request, 'index.html', {'products':products})


def details(request, pk):
    products = Menu.objects.get(pk=pk)
    return render(request, 'details.html', {'products':products})

# Create your views here.
