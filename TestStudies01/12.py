'''
4. Faça um programa que leia o nome e peso de 3 pessoas e no final mostre o
nome da pessoa mais pesada e a mais leve;
'''

pessoas = []
pesos = []

for i in range(3):
    nome = str(input(f"Entre com o nome da pessoa {i + 1}: "))
    peso = float(input(f"Entre com o peso da pessoa {i + 1}: "))

    pessoas.append([nome, peso])
    pesos.append(peso)

print(pessoas)
print(pesos)

mais_pesada = max(pesos)
mais_leve = min(pesos)

for pessoa in pessoas:

    if pessoa[1] == mais_pesada:
        print(f"A pessoa mais pesada é {pessoa[0]}")

    if pessoa[1] == mais_leve:
        print(f"A pessoa mais leve é {pessoa[0]}")