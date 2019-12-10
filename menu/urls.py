from django.urls import path
from . import views

urlpatterns=[
    path('', views.menu, name='menu'),
    path('details/<int:pk>', views.details, name='details')
]