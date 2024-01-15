'''
Desenvolva um código Python que lê do teclado nome e a idade atual 
de uma pessoa. Como saída, imprima o ano em que a pessoa 
completará 100 anos de idade.
'''


import datetime

nome = input()
idade = int(input())
ano_atual = datetime.datetime.now().year
ano_nascimento = ano_atual - idade
ano_100 = ano_nascimento + 100

print(ano_100)
