'''
2. Crie dois conjuntos, um para cada loja. Identifique quais modelos de
smartphones cada uma delas vendem. Em seguida, mostre quais
modelos no total você terá opção de comprar se visita-las e quais
modelos se encontram disponíveis em ambas as lojas;
'''

loja1 = {'Iphone 16', 'Iphone 16 pro max', 'Iphone 15 plus', 'Galaxy s25'}
loja2 = {'Galaxy s25', 'Galaxy s26 fe', 'Galaxy s21', 'iphone 15 plus'}

total_modelos = loja1 | loja2
print(f'Modelos disponiveis: {total_modelos}')

modelo_em_ambas = loja1 & loja2
print(f'Os modelos disponiveis em ambas as lojas são: {modelo_em_ambas}')