from django.urls import path
from . import views

urlpatterns=[
   path('<int:pk>', views.pay, name='order'),
   path('cartOrder', views.payCart, name='cartOrder')
]