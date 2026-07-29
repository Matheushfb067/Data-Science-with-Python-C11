'''
7. Faça um programa que leia uma palavra. Esse programa deve
percorrer a palavra e imprimir cada letra em maiúsculo, uma letra por
linha. No final, deverá informar quantas vogais a palavra tem e se a
letra ‘A’ está presente nela
'''
palavra = str(input('Entre com uma palavra: '))

num_vogais = 0 
tem_a = False

for l in palavra: 
    print(l.upper())

    if(l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u'):
        num_vogais += 1

    if l == 'A' or l == 'a': 
        tem_a = True
        
print(num_vogais)

if tem_a == True: 
    print("A letra A está presente na palavra")
else: 
    print("A letra A não está presente na palavra")