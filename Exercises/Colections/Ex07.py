'''
7. Usando a lista de ingredientes já preenchida para
a receita de bolo, agora crie mais dois conjuntos representando 
os ingredientes que duas pessoas diferentes têm em casa. Mostre quais 
ingredientes da receita ainda faltam comprar pelas pessoas para se fazer
o bolo.
'''
ingredientes = ['Farinha', 'Fermento', 'Ovo', 'Leite', 'Açucar', 'Cenoura', 'Chocolate']

ingredientes_receita = set(ingredientes) # transformando em conjunto

ingredientes_pessoa1 = {'Farinha', 'Ovo'}
ingredientes_pessoa2 = {'Cenoura', 'Chocolate', 'Leite'}

faltam_pessoa1 = ingredientes_receita - ingredientes_pessoa1
print(f'Ingredientes que a pessoa 1 ainda precisa comprar: {faltam_pessoa1}')

faltam_pessoa2 = ingredientes_receita - ingredientes_pessoa2
print(f'Ingredientes que a pessoa 1 ainda precisa comprar: {faltam_pessoa2}')