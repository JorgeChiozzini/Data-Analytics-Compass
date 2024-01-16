'''
Apresente o ator/atriz com a maior média de receita de bilheteria 
bruta por filme do conjunto de dados. Considere a coluna Avarage 
per Movie para fins de cálculo.
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
lista.sort(key=lambda x: x['media'], reverse=True)
print(f"O ator com maior média por filme é {lista[0]['nome']} com {lista[0]['media']} de média.")

with open("resultado3.txt", "a") as file:
    file.write(f"\nO ator/atriz com a maior média de receita de bilheteria bruta por filme é {lista[0]['nome']} com {lista[0]['media']} de média.")