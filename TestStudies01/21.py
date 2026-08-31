'''
5. Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros
entre 1 e 50 (use seed = 10 antes) 
a) Mostre o resultado da média de cada linha e cada coluna da matriz
gerada
b) Apresente o maior valor das médias das linhas e também das colunas
c) Mostre a quantidade de aparições de cada um dos números gerados na
matriz. Em seguida, mostre apenas os números que aparecem 2 vezes
'''
import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 51, [4, 4])
print(mtz)

soma_linha = mtz.sum(axis = 1)
media_linha = soma_linha / 4
print(media_linha)

soma_coluna = mtz.sum(axis = 0)
media_coluna = soma_coluna / 4

maior_media_linha = media_linha.max()
print(maior_media_linha)

maior_media_coluna = media_coluna.max()
print(maior_media_coluna)

print(np.unique(mtz))
print(np.unique(mtz, return_counts = True))