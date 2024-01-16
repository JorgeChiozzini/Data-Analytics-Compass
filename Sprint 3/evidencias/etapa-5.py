'''
Apresente a lista dos atores ordenada pela receita bruta de bilheteria 
de seus filmes (coluna Total Gross), em ordem decrescente.
Ao escrever no arquivo, considere o padrão de saída <nome do ator>
-  <receita total bruta>, adicionando um resultado a cada linha.
'''


def extrai(): 
    with open("actors.csv", "r", encoding="utf8") as file:
        lista = []
        contador = 0
 
        for line in file.readlines():
            ator = {}
 
            if contador == 0:
                contador += 1
                continue
 
            item = line.split(",")
 
            if len(item) > 6:
                item_diferente = line.split('"')
                novo = item_diferente[1].replace(",", "") + item_diferente[2]
                item = novo.split(",")
 
                for i in item:
                    i.strip()
 
            ator['nome'] = item[0]
            ator['total'] = float(item[1])
            ator['filmes'] = int(item[2])
            ator['media'] = float(item[3])
            ator['1 filme'] = item[4]
            ator['bruto'] = float(item[5])
 
            lista.append(ator)
    return lista
 
lista = extrai()

lista = extrai()
lista.sort(key=lambda x: x['total'], reverse=True)

for ator in lista:
    print(f"{ator['nome']} -  {ator['total']}")

 
with open("resultado5.txt", "a") as file:
    for ator in lista:
        file.write(f"\n{ator['nome']} -  {ator['total']}")

