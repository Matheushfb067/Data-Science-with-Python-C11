'''
8. Crie um dicionário para armazenar os dados de um produto (nome, preço e quantidade em estoque). 
Peça ao usuário os dados de 3 produtos diferentes e guarde cada dicionário em uma lista. No final, 
percorra a lista e mostre, para cada produto, seu nome e o valor total em estoque (preço × quantidade).
'''

lista_produtos = []

for i in range(3): 
    nome = str(input("Entre com o nome do produto: "))
    preco = float(input("Entre com o preço do produto: "))
    quantidade = int(input("Entre com a quantidade em estoque do produto: "))

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    lista_produtos.append(produto)

print("")
print(lista_produtos)
print("")

for produto in lista_produtos:
    valor_total_estoque = produto['preco'] * produto['quantidade']
    print(f'Produto: {produto['nome']} - Valor Total em Estoque: {valor_total_estoque}')