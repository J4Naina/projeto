from django.shortcuts import render
from django.views.generic import ListView
from models import Produto

class Home(ListView):
    model = Produto
    template_name = 'produtos/home.html'