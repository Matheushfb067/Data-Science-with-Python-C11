'''
3. Faça um programa que leia o sexo de uma pessoa e diga se ela é
homem (caso seja digitado M) ou mulher (caso seja digitado F). Caso
seja digitado algo inválido, continue perguntando até que o usuário
entre com um sexo válido
'''

genero = str(input("Entre com seu sexo (M ou F): ")).upper()
while(genero != 'M' and genero != 'F'): 
    genero = str(input("Entre com seu sexo (M ou F): ")).upper()

if(genero == 'M'): 
    print("Você é homem!")
else:
    print("Você é mulher!")