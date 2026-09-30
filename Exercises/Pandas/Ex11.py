'''
3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização 
(Literacy (%)) de cada região do planeta
'''

import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

grupo_regiao = ds.groupby('Region')
media_alfabetizacao = grupo_regiao['Literacy (%)'].mean()

print(f'A média de alfabetização de cada região é: {media_alfabetizacao.round(2)}')