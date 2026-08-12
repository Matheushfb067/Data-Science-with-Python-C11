'''
3. Mini Campo Minado
    a) Crie um NumPy Array 2 x 2 formado apenas por 0’s
    b) Em seguida, adicione um número 1 em uma posição aleatória desta matriz;
    c) Faça uma entrada de dados para solicitar o usuário que faça uma jogada (selecione uma posição da matriz) 
        I. Se ele selecionar todas as posições em que o número 1 não se encontra, mostre a mensagem
           “Congratulations ! You beat the game!:)”
        II. Senão, se dentro das 3 primeiras jogadas ele achar o número 1, mostre a mensagem
            “Game Over!:( Try Again!”
'''

import numpy as np

campo = np.zeros([2, 2])

# Sorteia uma linha e uma coluna aleatórias entre 0 e 1
linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)

campo[linha, coluna] = 1 # seta o valor aleatorio como um na linha/coluna
print(campo)

jogadas = []

while(len(jogadas) < 3):
    lin_jogada = int(input('Escolha uma Linha (0 ou 1): '))
    col_jogada = int(input('Escolha uma Coluna (0 ou 1): '))

    if lin_jogada < 0 or lin_jogada > 1 or col_jogada < 0 or col_jogada > 1:
        print('Posição inválida! Escolha apenas 0 ou 1.')
        continue

    if (lin_jogada, col_jogada) in jogadas: 
        print('Você já escolheu essa posição!')
        continue # volta o loop para o inicio

    jogadas.append((lin_jogada, col_jogada)) # salva a posição onde o jogador escolheu dentro da lista

    if campo[lin_jogada, col_jogada] == 1:
        print('Game Over!:( Try Again!')
        break
    elif campo[lin_jogada, col_jogada] == 0: 
        print('Boa! Jogada Segura, Continue...')

if(len(jogadas) == 3):
    print('Congratulations ! You beat the game! :)')

        


