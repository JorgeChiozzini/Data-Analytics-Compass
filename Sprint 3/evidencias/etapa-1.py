'''
Apresente o ator/atriz com maior número de filmes e a respectiva 
quantidade. A quantidade de filmes encontra-se na coluna 
Number of Movies do arquivo.
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
lista.sort(key=lambda x: x['filmes'], reverse=True)
print(f"O ator com maior número de filmes é {lista[0]['nome']} com {lista[0]['filmes']} filmes.")

with open("resultado.txt", "w") as file:
    file.write(f"O ator com maior número de filmes é {lista[0]['nome']} com {lista[0]['filmes']} filmes.")

