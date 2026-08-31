'''
4. Desenvolva um script que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens
até 200Km e R$0.45 para viagens mais longas
'''

distancia = float(input("Entre com a distancia em km: "))

if (distancia <= 200): 
    passagem = distancia * 0.5
else: 
    passagem = distancia * 0.45

print(passagem)