'''
2. Mostre a tabuada de um número que o usuário escolher dentro de um
intervalo específico também escolhido por ele
'''

num = float(input("Entre com um numero: "))
inferior = int(input("Entre com o limite inferior: "))
superior = int(input("Entre com o limite superior: "))


for i in range (inferior, superior + 1): 
    print(num, ' x ', i, ' = ', num * i)