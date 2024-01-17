'''
Apresente a média de receita de bilheteria bruta dos principais 
filmes, considerando todos os atores. Estamos falando aqui da 
média da coluna Gross.
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

media = sum(item['gross'] for item in lista)/len(lista)

print(f"A média de receita de bilheteria bruta dos principais filmes é de {media}.")

with open("resultado2.txt", "w") as file:
    media = sum(item['gross'] for item in lista)/len(lista)
    file.write(f"A média de receita de bilheteria bruta dos principais filmes é de {media}.")
