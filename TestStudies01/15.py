'''
7. Usando a lista de ingredientes já preenchida para a receita de bolo, agora crie 
mais dois conjuntos representando os ingredientes que duas pessoas diferentes têm em casa. 
Mostre quais ingredientes da receita ainda faltam comprar pelas pessoas para se fazer o bolo.
'''

ingredientes = ['Farinha', 'Ovo', 'Leite', 'Fermento', 'Chocolate', 'Açucar']

ingredientes = set(ingredientes)

pessoa1 = {'Farinha', 'Ovo', 'Fermento', 'Chocolate'}
pessoa2 = {'Farinha', 'Ovo', 'Leite'}

faltam_pessoa2 = ingredientes - pessoa2
faltam_pessoa1 = ingredientes - pessoa1

print(faltam_pessoa1)
print(faltam_pessoa2)