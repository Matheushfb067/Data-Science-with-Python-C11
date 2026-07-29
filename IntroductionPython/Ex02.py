'''
2. Mostre a tabuada de um número que o usuário escolher dentro de um
intervalo específico também escolhido por ele
'''

num = float(input("Entre com um numero: "))

for i in range (1, 11): 
    mult = i * num
    print('{} x {} = {}'.format(i, num, mult))