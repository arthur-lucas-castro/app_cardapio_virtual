from django.db import models

class Cliente(models.Model):
    nome=models.CharField(max_length=30)
    cpf=models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.nome)

class Categoria(models.Model):
    nome=models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.nome)
  
class Produto(models.Model):
    nome=models.CharField(max_length=30)
    preco= models.DecimalField(decimal_places=2, max_digits=5)
    descricao=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default=1)
    imagem = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.nome)

class Pedido(models.Model):
    clinteId = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    mesa=models.IntegerField()
    ativo = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.mesa)

class PedidoProduto(models.Model):
    produtoId = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, null=True)
    pedidoId = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING, null=True)
    mesa=models.IntegerField()
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.mesa)



