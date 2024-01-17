'''
Apresente a lista dos atores ordenada pela receita bruta de bilheteria 
de seus filmes (coluna Total Gross), em ordem decrescente.
Ao escrever no arquivo, considere o padrão de saída <nome do ator>
-  <receita total bruta>, adicionando um resultado a cada linha.
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
lista.sort(key=lambda x: x['total'], reverse=True)


for ator in lista:
    print(f"{ator['actor']} -  {ator['total']}")

 
with open("resultado5.txt", "w") as file:
    for ator in lista:
        file.write(f"{ator['actor']} -  {ator['total']}\n")

