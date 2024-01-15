'''
Escreva um código Python para imprimir todos os números primos 
entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo 
que identifica se um número é primo ou não.
Importante: Aplique a função range().
'''


def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos():
    for numero in range(2, 101):
        if is_primo(numero):
            print(numero)

imprimir_primos()
