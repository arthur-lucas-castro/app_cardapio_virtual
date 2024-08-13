from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente

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
    print(produtos)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Aqui você pode implementar a lógica para adicionar o produto ao carrinho.
    # Exemplo: salvar na sessão do usuário
    carrinho = request.session.get('carrinho', {})
    
    if produto_id in carrinho:
        carrinho[produto_id]['quantidade'] += 1
    else:
        carrinho[produto_id] = {'nome': produto.nome, 'preco': str(produto.preco), 'quantidade': 1}
    
    request.session['carrinho'] = carrinho
    
    return redirect('listar_produtos')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    return render(request, 'produtos/ver_carrinho.html', {'carrinho': carrinho})