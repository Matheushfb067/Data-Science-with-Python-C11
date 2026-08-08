'''
5. Desenvolva um programa que leia o nome, idade e sexo de
n pessoas. No final, mostre: 
a. A média de idade do grupo;
b. Quantas mulheres têm menos de 20 anos.
Dica: em Python, os operadores booleanos básicos são and, or
e not.
'''

# Entrada de dados
num_pessoas = int(input('Entre com o numero de pessoas: '))

pessoas = []

for i in range(num_pessoas): 
    nome = str(input(f'Entre com o nome da pessoa {i+1}: '))
    idade = int(input(f'Entre com a idade da pessoa {i+1}: '))
    sexo = str(input(f"Entre com o sexo da pessoa {i+1} ('M' e 'F'): ")).upper()

    while sexo != 'M' and sexo != 'F': 
        print('Sexo invalido! Entre com M ou F.')
        sexo = str(input(f"Entre com o sexo da pessoa {i+1} ('M' e 'F'): ")).upper()

    pessoas.append([nome, idade, sexo])

print(pessoas)

# Média das idades do grupo e Quantas mulheres tem menos 

soma_idades = 0

for pessoa in pessoas: 
    soma_idades += pessoa[1]

media = soma_idades / num_pessoas

print(f'A média das idades é: {media:.2f}')

# Quantas mulheres tem menos de 20 anos

contador = 0
for pessoa in pessoas: 
    if(pessoa[2] == 'F' and pessoa[1] < 20 ):
        contador += 1

print(f'O Numero de mulheres com menos de 20 anos é: {contador}')