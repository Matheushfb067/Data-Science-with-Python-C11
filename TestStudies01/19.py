'''
3. Mini Campo Minado

a) Crie um NumPy Array 2 x 2 formado apenas por 0's.

b) Em seguida, adicione o número 1 em uma posição aleatória dessa matriz.

c) Solicite ao usuário que faça uma jogada, selecionando uma posição da matriz:

   I. Se ele selecionar todas as posições em que o número 1 não se encontra,
      mostre a mensagem: "Congratulations! You beat the game! :)"

   II. Caso ele encontre o número 1 dentro das três primeiras jogadas, mostre
       a mensagem: "Game Over! :( Try Again!"
'''

import numpy as np

# Criei o campo
mtz = np.zeros([2, 2]).astype(int)

# Sorteei uma linha e uma coluna
linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)

# O campo está recebendo o 1 em uma posição da linha ou coluna
mtz[linha, coluna] = 1
print(mtz)

jogadas = []
perdeu = False

while(len(jogadas) < 3):
    linha_jogada = int(input("Entre com uma linha 0 ou 1: "))
    coluna_jogada = int(input("Entre com uma coluna 0 ou 1: "))

    # Validando Entradas: 
    if linha_jogada < 0 or linha_jogada > 1 or coluna_jogada < 0 or coluna_jogada > 1:
        print('Posição inválida! Escolha apenas 0 ou 1.')
        continue

    # Validando se uma linha ou coluna já foi escolhida
    if [linha_jogada, coluna_jogada] in jogadas:
        print('Você já escolheu essa posição!')
        continue 

    jogadas.append([linha_jogada, coluna_jogada])

    if([linha_jogada, coluna_jogada]) == 1:
        print("Game Over! :( Try Again!")
        perdeu = True
        break
    elif [linha_jogada, coluna_jogada] == 0: 
            print('Boa! Jogada Segura, Continue...')

if(len(jogadas) == 3 and perdeu == False):
    print('Congratulations! You beat the game! :)')