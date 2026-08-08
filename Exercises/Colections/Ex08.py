'''
8. Crie um dicionário para armazenar os dados de um produto (nome, preço e quantidade em estoque). 
Peça ao usuário os dados de 3 produtos diferentes e guarde cada dicionário em uma lista. No final, 
percorra a lista e mostre, para cada produto, seu nome eo valor total em estoque (preço × quantidade).
'''

lista_produtos = []

for i in range(3): 
    nome = str(input('Entre com o nome do produto: '))
    preco = float(input('Entre com o preço do produto: '))
    quantidade = int(input('Entre com a quantidade do produto: '))

    produto = {
        'nome': nome,
        'preço': preco,
        'quantidade': quantidade 
    }

    lista_produtos.append(produto)

print(lista_produtos)

for produto in lista_produtos: 
    valor_total = produto['preço'] * produto['quantidade']
    print(f'Produto: {produto['nome']} - Valor total em estoque: {valor_total:.2f}')