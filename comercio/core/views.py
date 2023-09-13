from django.shortcuts import render
from django.views.generic import ListView
from core import Produto

class Home(ListView):
    model = Produto
    template_name = 'core/home.html'