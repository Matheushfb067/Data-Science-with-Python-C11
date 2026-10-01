'''
7. Por meio do dataset paises.csv, trace em uma mesmo plano cartesiano 
duas linhas com estilos customizados (marcador, cor e tipo de linhas 
diferentes) comparando o “GDP ($ per capita)” e o número de “Phones
(per 1000)” dos países da Europa Ocidental (WESTERN EUROPE);
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')

europa_ocidental = ds[ds['Region'].str.strip() == 'WESTERN EUROPE']

plt.plot(europa_ocidental['Country'], europa_ocidental['GDP ($ per capita)'], 'ro-')
plt.plot(europa_ocidental['Country'], europa_ocidental['Phones (per 1000)'], 'b--')

plt.xlabel('Países')
plt.ylabel('GDP per capita / Telefones por 1000 habitantes')

plt.show()