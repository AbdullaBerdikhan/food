from django.urls import path
from . import views

urlpatterns=[
    path('cart/<int:pk>', views.addCart, name='addtocart'),
    path('basket', views.showCart, name='showcart'),
    path('delete/<int:pk>', views.delete, name='delete')

]