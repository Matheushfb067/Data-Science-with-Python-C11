'''
2. Os valores das Series criadas na Questão 1 representam as fatias de
mercado (porcentagem) de 3 linguagens de programação populares em dois 
anos consecutivos. Para cada ano, apresente a porcentagem total que elas 
juntas representam no mercado;
'''

import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print(f"Porcentagem total do ano 1: {totalAno1} %")
print(f"Porcentagem total do ano 2: {totalAno2} %")