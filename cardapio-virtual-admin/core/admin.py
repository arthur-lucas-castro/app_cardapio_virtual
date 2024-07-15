from django.contrib import admin
from admin_thumbnail import thumb_admin
from .models import Produto, Pedido, Cliente, Categoria


admin.site.register(Categoria)

@admin.register(Produto)
@admin_thumbnails.thumbnail('imagem')
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail','nome', 'preco', 'categoria')
    list_filter = ('categoria',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    actions_on_top = False
    

