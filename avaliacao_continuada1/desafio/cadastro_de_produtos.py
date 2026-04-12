# SOBRE A APLICAÇÃO
# Desenvolva um CRUD de produtos utilizando while no menu e 
# for para listar ou buscar produtos
# Apenas serão permitidos os métodos de lista 
# append (adicionar) e pop (remover a partir de um índice)
# A aplicação deve ser executada até que o valor da opção seja 0
# Caso o valor da opção não exista, informar ao usuário


# DADOS
# O produto deve ter os dados Nome (string) e Preço (float)


# FUNCIONALIDADES
# O sistema deve ter as funções:

# 1 - listarProdutos: Retorna todos os produtos cadastrados 
#       > Dados de entrada: nenhum
#       > Leia todos os produtos
#       > Retorno: lista de produtos

# 2 - adicionarProduto: 
#       > Dados de entrada: dict Produto(nome, preco)
#       > Adiciona um produto (use append)
#       > Retorno: True ou False

# 3 - buscarProduto: 
#       > Dados de entrada: nome do produto (string)
#       > Retorne o índice do produto encontrado, ou None se não for encontrado nenhum item
#       > Retorno: o índice do produto

# 4 - atualizarProduto: Atualiza os dados de um produto
#       > Dados de entrada: índice (int), dict do novo Produto(nome, preco)
#       > Atualiza os dados de um produto já existente
#       > Retorno: True ou False

# 5 - removerProduto: Dado o índice do produto, ele deve ser removido da lista 
#       > Dados de entrada: índice (int)
#       > Remove o produto do índice
#       > Retorno: True ou False

# IMPORTANTE: Ignore os erros de execução. Em funções como atualizar e remover, apenas passe como
# parâmetros índices de produtos existentes.

produtos = [
  {'nome': 'Fatia de Bolo', 'preco': 20.00},
  {'nome': 'Pão na chapa', 'preco': 12.00},
  {'nome': 'Misto quente', 'preco': 15.00},
  {'nome': 'Café expresso', 'preco': 12.00},
  {'nome': 'Capuccino', 'preco': 18.00},
  {'nome': 'Café Latte', 'preco': 18.00}

] #Exemplo de item {nome: Arroz, preco: 30.00}

def listarProdutos():
    if(len(produtos) == 0):
        print('Não tem produtos cadastrados')
    else:
        for i in range(len(produtos)):
            p = produtos[i]
            print(f"{i} - {p['nome']} ... R$ {p['preco']:.2f}")
        
        
def adicionarProduto(produto):
    produtos.append(produto)
    return True


def buscarProduto(produtoNome):
    for i in range(len(produtos)):
        if produtos[i]['nome'] == produtoNome:
           return i
    return None


def atualizarProduto(indice, produto):
    produtos[indice] = produto
    return True


def removerProduto(indice):
    produtos.pop(indice)
    return True



opcao = None
while(opcao != '0'):
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Listar Produtos')
    print('2 - Adicionar Produto')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('0 - Sair')
    print('========================================')

    opcao = input('Opção desejada:')
    
    if(opcao == '1'): 
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '2'): 
        print()
        print('ADICIONAR DE PRODUTOS ==================')
        nome = input('Nome:')
        preco = float(input('Preço:'))
        adicionarProduto({'nome': nome, 'preco': preco})
        print('Produto adicionado')
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '3'): 
         print('BUSCAR PRODUTO =========================')
         nome = input('Busque o produto desejado:')
         indice = buscarProduto(nome)

         if indice == None:
            print('Produto não encontrado')
         else:
            print('Produto encontrado', produtos[indice])

    
    elif(opcao == '4'): 
         print('ATUALIZAR PRODUTO ======================')
         indice = (int(input('indice do produto: ')))
         nome = input('Novo nome')
         preco = float(input('Novo preço: '))
         atualizarProduto(indice, {'nome': nome, 'preco': preco})
         print('Produto atualizado')
    
    elif(opcao == '5'): 
         print('REMOVER PRODUTO ========================')
         indice = int(input('índice do produto: '))
         removerProduto(indice)
         print('Produto removido')
    
    elif(opcao != None): 
        print('Opção não existe')    
