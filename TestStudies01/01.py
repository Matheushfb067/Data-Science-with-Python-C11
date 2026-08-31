'''
1. Crie um programa que leia seu nome completo e mostre:
• Seu nome com todas as letras maiúsculas
• Seu nome com todas as letras minúsculas
• Quantas letras ao todo tem seu nome
• E como seria se trocássemos seu último nome para “do Inatel”
'''

nome = str(input("Entre com seu nome: "))

maiusculas = nome.upper()
print(maiusculas)

# ===========================================

minusculas = nome.lower()
print(minusculas)

# ===========================================

quantidade = len(nome)
print(quantidade)

# ===========================================

partes = nome.split() # #quebra o texto em partes
ultimo_nome = partes[-1]

troca = nome.replace(ultimo_nome, 'do Inatel')
print(troca)