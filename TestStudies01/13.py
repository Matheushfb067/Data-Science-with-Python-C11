'''
5. Desenvolva um programa que leia o nome, idade e sexo de
n pessoas. No final, mostre:
a. A média de idade do grupo;
b. Quantas mulheres têm menos de 20 anos.

Dica: em Python, os operadores booleanos básicos são and, or e not
'''

num = int(input("Entre com o numero de pessoas: "))

pessoas = []
soma_idades = 0
mulheres_menores_vinte = 0

for i in range(num): 
    nome = str(input(f"Entre com o nome da pessoa {i + 1}: "))
    idade = int(input(f"Entre com a idade da pessoa {i + 1}: "))
    sexo = str(input(f"Entre com o sexo da pessoa {i + 1} (M ou F) :")).upper()

    while(sexo != 'M' and sexo != 'F'):
        sexo = str(input(f"Entre com o sexo da pessoa {i + 1} (M ou F) :")).upper()

    pessoas.append([nome, idade, sexo])

    soma_idades += idade

    if sexo == 'F' and idade < 20: 
        mulheres_menores_vinte += 1

print("")
print(pessoas)
print("")

media = soma_idades / num

print(f"A média das idades é: {media}")
print(f'A quantidade de mulheres com menos de 20 anos é: {mulheres_menores_vinte}')