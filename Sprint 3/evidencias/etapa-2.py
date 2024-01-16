'''
Apresente a média de receita de bilheteria bruta dos principais 
filmes, considerando todos os atores. Estamos falando aqui da 
média da coluna Gross.
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
lista.sort(key=lambda x: x['bruto'], reverse=True)
print(f"A média de receita de bilheteria bruta dos principais filmes é de {sum(item['bruto'] for item in lista)/len(lista)}.")

with open("resultado2.txt", "w") as file:
    file.write(f"A média de receita de bilheteria bruta dos principais filmes é de {sum(item['bruto'] for item in lista)/len(lista)}.")
