'''
Escreva uma função que recebe uma string de números separados por
vírgula e retorne a soma de todos eles. Depois imprima a 
soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
'''


def somar_valores(string):
    valores = string.split(',')
    soma = 0
    for valor in valores:
        soma += int(valor)
    return soma

string = "1,3,4,6,10,76"
soma = somar_valores(string)
print(soma)
