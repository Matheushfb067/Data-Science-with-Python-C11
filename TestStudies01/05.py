'''
5. Faça um programa que leia um número entre 1000 e 9999
e mostre na tela 
• qual o número da unidade
• número da dezena 
• número da centena 
• E número do milhar 
'''

num = int(input("Entre com um numero entre 1000 e 9999: "))
while(num < 1000 or num > 9999):
    num = int(input("Entre com um numero entre 1000 e 9999: "))

num = str(num)

print(f"O numero da unidade é: {num[3]}")
print(f"O numero da unidade é: {num[2]}")
print(f"O numero da unidade é: {num[1]}")
print(f"O numero da unidade é: {num[0]}")