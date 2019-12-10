from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import NewForm


class Register(generic.CreateView):
    form_class = NewForm
    model = User
    success_url = reverse_lazy('menu')
    template_name = 'registration/register.html'


# Create your views here.
