'''
7. Crie uma função customizada que receba a coluna Infant mortality (per 1000 births) 
de um país e retorne o valor reduzido em 15% (simulando assim uma meta de redução da 
mortalidade infantil). Aplique esta função à coluna usando o método apply() e, em seguida, 
concatene a coluna original com a coluna resultante lado a lado para se fazer uma comparação;
'''

import pandas as pd 
import numpy as np 

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print()

def reducao_mortalidade(x):
    return x * 0.15

mortalidade_infantil = ds['Infant mortality (per 1000 births)']
mortalidade_reduzida = mortalidade_infantil.apply(reducao_mortalidade)

comparacao = pd.concat([mortalidade_infantil, mortalidade_reduzida.rename('Infant mortality (per 1000 births) -15%')], axis = 1)
print(comparacao)