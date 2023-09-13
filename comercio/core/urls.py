from django.urls import path
from . views import Produto
app_name= 'core'

urlpatterns = [
    path('', Produto.as_view(), name='home'),
]