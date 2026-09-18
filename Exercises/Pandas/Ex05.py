'''
5. Se estas porcentagens de crescimento/declínio se mantivessem iguais
para os próximos 2 anos, qual seria a linguagem mais popular?
Dica: useo método nlargest(1) no final para retornar rapidamente
a label e maior valor de uma Series.
'''

import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

variacao = seriesAno2 - seriesAno1

seriesAno3 = seriesAno2 + variacao
seriesAno4 = seriesAno3 + variacao

print(seriesAno3)
print("")
print(seriesAno4)
print("")

maisPopular = seriesAno4.nlargest(1)
print(f'A linguagem mais popular é: {maisPopular}')