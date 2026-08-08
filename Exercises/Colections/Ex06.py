'''
6. Crie uma lista com ingredientes de uma receita de bolo:
a. Adicione um novo ingrediente no final;
b. Insira outro em uma posição específica;
c. Remova um ingrediente pelo valor.
'''
ingredientes = ['farinha', 'Fermento', 'Ovo']
print(ingredientes)

ingredientes.append('Leite')
print(ingredientes)

ingredientes.insert(1, 'Açucar')
print(ingredientes)

ingredientes.remove('Ovo')
print(ingredientes)