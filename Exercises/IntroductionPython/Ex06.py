'''
6 . Peça ao usuário para entrar com um número decimal. Em seguida,
aplique e mostreo resultado:
• da raiz quadrada deste número • função teto • função chão • sua parte inteira

'''
import math

num = float(input("Entre com um numero decimal: "))

print(math.sqrt(num))
print(math.ceil(num))
print(math.floor(num))
print(math.trunc(num))

