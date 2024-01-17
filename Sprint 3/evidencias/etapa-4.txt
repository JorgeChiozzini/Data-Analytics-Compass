'''
A coluna #1 Movie contém o filme de maior bilheteria em que o ator 
atuou. Realize a contagem de aparições destes filmes no dataset, 
listando-os ordenados pela quantidade de vezes em que estão 
presentes. Considere a ordem decrescente e, em segundo nível, o 
nome do  filme. Ao escrever no arquivo, considere o padrão de 
saída <sequencia> - O filme <nome filme> aparece <quantidade> 
vez(es) no dataset, adicionando um resultado a cada linha.
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

filmes_cont = {}
for filmes in lista:
        nome_filme = filmes ['1 movie']
        if nome_filme in filmes_cont:
            filmes_cont[nome_filme] += 1
        else:
            filmes_cont[nome_filme] = 1

filmes_cont = dict(sorted(filmes_cont.items(), key=lambda x: x[1], reverse=True))

for index, (filmes, num_filmes) in enumerate(filmes_cont.items()):
    print(f"{index + 1} - O filme {filmes} aparece {num_filmes} vez(es) no dataset")


with open("resultado4.txt", "w") as file:
    for index, (filmes, num_filmes) in enumerate(filmes_cont.items()):
        file.write(f"{index + 1} - O filme {filmes} aparece {num_filmes} vez(es) no dataset\n")



    
