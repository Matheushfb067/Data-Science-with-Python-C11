'''
3. Faça um programa que leia o sexo de uma pessoa e diga se ela é
homem (caso seja digitado M) ou mulher (caso seja digitado F). Caso
seja digitado algo inválido, continue perguntando até que o usuário
entre com um sexo válido
'''

gender = str(input('Entre com M ou F para indicar o sexo: '))

while gender != 'M' and gender != 'F':
    print('Sexo invalido! Digite M ou F.')
    gender = str(input('Entre com M ou F para indicar o sexo: '))

    if gender == 'M': 
        print('Você é Homem!')
    else: 
        print('Vocẽ é Mulher!')