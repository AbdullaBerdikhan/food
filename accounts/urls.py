from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import Register

urlpatterns=[
    path('register', Register.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]