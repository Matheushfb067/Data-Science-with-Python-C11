'''
1. Crie uma lista preenchida com os 5 primeiros colocados de um
Campeonato de Futebol, na ordem de colocação. Depois mostre:
a. Apenas os 3 primeiros colocados;
b. Os últimos 2 colocados;
c. Uma lista com os times em ordem alfabética;
d. Em que posição da tabela se encontrao Barcelona;
'''

colocados = ['Barcelona', 'Real Madrid', 'Juventus', 'Liverpool', 'Manchester City']

print(colocados[:3])
print(colocados[3:])
print(sorted(colocados))

posicao = 0
for time in colocados: 
    if time == 'Barcelona':
        print(posicao)
        break
    posicao += 1