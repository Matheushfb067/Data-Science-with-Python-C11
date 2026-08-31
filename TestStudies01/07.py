'''
7. Faça um programa que leia uma palavra. Esse programa deve
percorrer a palavra e imprimir cada letra em maiúsculo, uma letra por
linha. No final, deverá informar quantas vogais a palavra tem e se a
letra ‘A’ está presente nela
'''

palavra = str(input(("Entre com uma palavra: ")))
num_vogais = 0
tem_a = False

for letra in palavra: 
    print(letra.upper())

    if(letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u'):
        num_vogais += 1

    if(letra == 'A' or letra == 'a'):
        tem_a = True

print(f"A palavra tem : {num_vogais} vogais")

if(tem_a == True):
    print("A palavra tem A")
else: 
    print("A palavra não tem A")