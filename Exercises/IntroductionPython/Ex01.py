'''
1. Crie um programa que leia seu nome completo e mostre:
• Seu nome com todas as letras maiúsculas
• Seu nome com todas as letras minúsculas
• Quantas letras ao todo tem seu nome
• E como seria se trocássemos seu último nome para “do Inatel”
'''

nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(len(nome))
print(len(nome.replace(' ', '')))

troca = nome.split()
troca[-1] = 'do Inatel'

novoNome = ' '.join(troca)
print(novoNome)