'''
Implemente a função my_map(list, f) que recebe uma lista como 
primeiro argumento e uma função como segundo argumento. 
Esta função aplica a função recebida para cada elemento da lista 
recebida e retorna o resultado em uma nova lista.
Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
e com uma função que faz potência de 2 para cada elemento.
'''

def my_map(lista, f):
    return [f(elemento) for elemento in lista]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_potencia = my_map(lista, lambda x: x**2)  

print(lista_potencia)

