
from django.urls import path
from .views import listar_produtos, adicionar_ao_carrinho, ver_carrinho, login

urlpatterns = [
    path('', login, name='login'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('adicionar-ao-carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
]
