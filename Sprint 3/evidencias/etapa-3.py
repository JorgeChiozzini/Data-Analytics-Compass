'''
Apresente o ator/atriz com a maior média de receita de bilheteria 
bruta por filme do conjunto de dados. Considere a coluna Avarage 
per Movie para fins de cálculo.
'''

def leitor_csv(): 
    with open("actors.csv", "r", encoding="utf8") as file:
        lista = []
        contador = 0
 
        for line in file.readlines():
            tabela = {}
 
            if contador == 0:
                contador += 1
                continue
 
            item = line.split(",")
 
            if len(item) > 6:
                problema = line.split('"')
                novo = problema[1].replace(",", "") + problema[2]
                item = novo.split(",")
 
                for i in item:
                    i.strip()
 
            tabela['actor'] = item[0]
            tabela['total'] = float(item[1])
            tabela['movies'] = int(item[2])
            tabela['average'] = float(item[3])
            tabela['1 movie'] = item[4]
            tabela['gross'] = float(item[5])
 
            lista.append(tabela)
    return lista
 
lista = leitor_csv()
lista.sort(key=lambda x: x['average'], reverse=True)
print(f"O ator com maior média por filme é {lista[0]['actor']} com {lista[0]['average']} de média.")

with open("resultado3.txt", "w") as file:
    file.write(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é {lista[0]['actor']} com {lista[0]['average']} de média.")
