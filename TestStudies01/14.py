'''
6. Crie uma lista com ingredientes de uma receita de bolo:
a. Adicione um novo ingrediente no final;
b. Insira outro em uma posição específica;
c. Remova um ingrediente pelo valor.
'''

ingredientes = ['Farinha', 'Ovo', "Leite"]
print(ingredientes)

ingredientes.append('Fermento')
print(ingredientes)

ingredientes.insert(2, 'Chocolate')
print(ingredientes)

ingredientes.remove('Ovo')
print(ingredientes)