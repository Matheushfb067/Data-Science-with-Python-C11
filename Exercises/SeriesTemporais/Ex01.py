import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


# Série temporal do tráfego aéreo de passageiros (observações mensais).
airtravel = pd.read_csv(
    'airtravel.csv',
    index_col='Date',
    parse_dates=True
)
airtravel = airtravel.asfreq('MS')

# Visualização da série original.
airtravel['Passengers'].plot(
    figsize=(10, 5),
    title='Passageiros do transporte aéreo internacional',
    xlabel='Data',
    ylabel='Número de passageiros',
    x_compat=True
)
plt.tight_layout()
plt.show()

# Decomposição multiplicativa: a amplitude da sazonalidade cresce junto com
# o nível da série. O período 12 representa os 12 meses de cada ano.
decomp_airtravel = seasonal_decompose(
    airtravel['Passengers'],
    model='multiplicative',
    period=12
)
decomp_airtravel.plot()
plt.suptitle('Decomposição da série de passageiros', y=1.02)
plt.tight_layout()
plt.show()

# Respostas:
# a) Sim. Há tendência crescente, aproximadamente exponencial, com aceleração
#    do crescimento ao longo do tempo.
# b) Sim. Há sazonalidade anual, com período de 12 meses; os valores tendem a
#    ser maiores no meio do ano e menores no início/fim do ano.
# c) Não há um ciclo econômico independente que possa ser afirmado apenas
#    pela série. A repetição regular observada é sazonalidade anual.


# Série temporal anual das emissões de CO2.
co2 = pd.read_csv('co2_emissions.csv', index_col='Year')
co2.index = pd.to_datetime(co2.index.astype(str), format='%Y')
co2.index.name = 'Date'
co2 = co2.asfreq('YS')

# Visualização da série original.
co2['CO2_Emissions'].plot(
    figsize=(10, 5),
    title='Emissões de CO2 por ano',
    xlabel='Ano',
    ylabel='Emissões de CO2',
    x_compat=True
)
plt.tight_layout()
plt.show()

# Como os dados são anuais, não há uma sazonalidade intra-anual observável.
# Usa-se período 8 para inspecionar oscilações de vários anos como possível
# ciclo. Esse período candidato não significa que os dados tenham sazonalidade.
decomp_co2 = seasonal_decompose(
    co2['CO2_Emissions'],
    model='additive',
    period=8
)
decomp_co2.plot()
plt.suptitle('Decomposição da série de emissões de CO2', y=1.02)
plt.tight_layout()
plt.show()

# Respostas:
# a) Sim. A tendência é predominantemente decrescente ao longo do período,
#    embora haja oscilações em torno dela.
# b) Não há sazonalidade identificável: cada observação representa um ano e,
#    portanto, não existem dados de meses ou estações dentro de cada ano.
# c) Há oscilações de vários anos, com picos e vales separados por cerca de
#    7–8 anos, compatíveis com um ciclo de longo prazo. Como a série é curta
#    (31 anos), esse ciclo é apenas uma indicação visual e não uma causa
#    demonstrada pelos dados; pode refletir variação/ciclo econômico ou outros
#    fatores externos.
