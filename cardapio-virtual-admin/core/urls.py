
from django.urls import path
from .views import listar_produtos, adicionar_ao_carrinho, ver_carrinho, login, realizar_pedido, pedido_realizado, listar_pedidos_ativos

urlpatterns = [
    path('', login, name='login'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('adicionar-ao-carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
    path('realizar-pedido/', realizar_pedido, name='realizar_pedido'),
    path('pedido-realizado/<int:pedido_id>/', pedido_realizado, name='pedido_realizado'),
    path('pedidos-ativos/', listar_pedidos_ativos, name='listar_pedidos_ativos'),

]
