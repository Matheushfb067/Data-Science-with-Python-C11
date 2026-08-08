'''
4. Faça um programa que leia o nome e peso de 3 pessoas
e no final mostre o nome da pessoa mais pesada e
a mais leve
'''

pessoas = []

for i in range(3): 
    nome = str(input(f'Entre com o nome da pessoa {i + 1}: '))
    peso = float(input(f'Entre com o peso da pessoa {i + 1}: '))

    pessoas.append([nome, peso])

mais_pesada = pessoas[0]

for j in pessoas: 
    if j[1] > mais_pesada[1]:
        mais_pesada = j

print(f'A pessoa mais pesada é {mais_pesada[0]} com {mais_pesada[1]}')