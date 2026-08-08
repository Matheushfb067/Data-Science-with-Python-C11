'''
3. Faça um programa que leia o nome e a média de um aluno
e guarde-os em um dicionário. Em seguida, a partir da média (para ser
aprovado deve ter média >= 50), gere a situação final do aluno (‘AP’
ou ‘RP’), que também deve ser guardada neste dicionário. No final,
mostre todo o conteúdo deste dicionário;
'''

nome = str(input('Entre com o nome do aluno: '))
media = float(input('Entre com a média do aluno: '))

aluno = {
    'nome': nome,
    'media': media
}

print(aluno)

if media >= 50: 
    situacao = 'AP'
else: 
    situacao = 'RP'

aluno['situação'] = situacao

print(aluno)