'''
6. Peça ao usuário para entrar com um número decimal. Em seguida,
aplique e mostre o resultado:
• da raiz quadrada deste número 
• função teto 
• função chão 
• sua parte inteira
'''
import math as mt

num = float(input("Entre com um numero decinal: "))

print(mt.sqrt(num))
print(mt.ceil(num)) 
print(mt.floor(num))
print(mt.trunc(num))