from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente, Pedido, PedidoProduto

def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']

        # Verifica se o cliente já existe pelo CPF
        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
            # Se o cliente já existe, salva o ID na sessão
            request.session['cliente_id'] = cliente.id
        else:
            # Se o cliente não existe, cria um novo e salva no banco de dados
            cliente = Cliente.objects.create(nome=nome, cpf=cpf)
            request.session['cliente_id'] = cliente.id

        # Redireciona para a página de produtos ou outra página
        return redirect('listar_produtos')

    return render(request, 'produtos/login.html')

def listar_produtos(request):
    produtos = Produto.objects.filter()
    carrinho = request.session.get('carrinho', {})
    carrinho_count = len(carrinho)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos, 'carrinho_count': carrinho_count})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Aqui você pode implementar a lógica para adicionar o produto ao carrinho.
    # Exemplo: salvar na sessão do usuário
    carrinho = request.session.get('carrinho', {})
    
    if produto_id in carrinho:
        carrinho[produto_id]['quantidade'] += 1
    else:
        carrinho[produto_id] = {'id': produto.id, 'nome': produto.nome, 'preco': str(produto.preco), 'quantidade': 1}
    
    request.session['carrinho'] = carrinho
    
    return redirect('listar_produtos')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    return render(request, 'produtos/ver_carrinho.html', {'carrinho': carrinho})

def realizar_pedido(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')  # Redireciona para login se o cliente não estiver autenticado

    cliente = Cliente.objects.get(id=cliente_id)
    print(cliente.id)
    
    if request.method == 'POST':
        mesa = request.POST['mesa']  # Supondo que o número da mesa seja fornecido

        # Cria o pedido e salva no banco de dados
        pedido = Pedido.objects.create(clienteId=cliente, mesa=mesa, ativo=True)

        # Recupera o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Cria registros em PedidoProduto para cada item no carrinho
        for item in carrinho.values():

            produto = Produto.objects.get(id=item['id'])
            PedidoProduto.objects.create(
                produtoId=produto,
                pedidoId=pedido,
                status=PedidoProduto.StatusPedidos.PEDIDO_REALIZADO
            )

        # Limpa o carrinho após realizar o pedido
        request.session['carrinho'] = {}  # Limpa o carrinho após realizar o pedido
        return redirect('pedido_realizado', pedido_id=pedido.id)  # Redireciona para uma página de confirmação

    return render(request, 'produtos/ver_carrinho.html')

def pedido_realizado(request, pedido_id):
    return render(request, 'produtos/pedido_realizado.html', {'pedido_id': pedido_id})

def listar_pedidos_ativos(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')  # Redireciona para login se o cliente não estiver autenticado

    pedidos_ativos = Pedido.objects.filter(clienteId=cliente_id, ativo=True).prefetch_related('pedidoproduto_set')
    
    context = {
        'pedidos_ativos': pedidos_ativos
    }
    return render(request, 'produtos/listar_pedidos_ativos.html', context)