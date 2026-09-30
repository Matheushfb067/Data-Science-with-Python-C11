'''
5. Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e 
retorne o texto ‘Balanced’ caso o valor seja < 9 e ‘Urgent’ caso contrário. Em 
seguida, crie um campo no Dataset chamado ‘Humanitarian Help’ que receba estes 
valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova 
coluna foi feita com sucesso.
'''

import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

def classificar_ajuda(taxa):
    if taxa < 9:
        return 'Balanced'
    else: 
        return 'Urgent'

ds['Humanitarian Help'] = ds['Deathrate'].apply(classificar_ajuda)
print(ds)