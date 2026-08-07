'''
4. Desenvolva um script que pergunte a distância de uma viagem em
Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens
até 200Km e R$0.45 para viagens mais longas
'''

distancia = float(input('Entre com a Distancia em Km da sua viagem: '))

if distancia <= 200: 
    preco = distancia * 0.50
else: 
    preco = distancia * 0.45

print(f'O preço da passagem é: {preco:.2f}')