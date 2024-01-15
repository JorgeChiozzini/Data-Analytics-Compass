'''
Escreva uma função que recebe uma lista e retorna uma 
nova lista sem elementos duplicados. 
Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']
'''

def remover_duplicados(lista):
    return list(set(lista))

minha_lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicados = remover_duplicados(minha_lista)

print(lista_sem_duplicados)
