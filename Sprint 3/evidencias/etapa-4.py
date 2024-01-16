'''
A coluna #1 Movie contém o filme de maior bilheteria em que o ator 
atuou. Realize a contagem de aparições destes filmes no dataset, 
listando-os ordenados pela quantidade de vezes em que estão 
presentes. Considere a ordem decrescente e, em segundo nível, o 
nome do  filme. Ao escrever no arquivo, considere o padrão de 
saída <sequencia> - O filme <nome filme> aparece <quantidade> 
vez(es) no dataset, adicionando um resultado a cada linha.
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

filmes_cont = {}
for filmes in lista:
        nome_filme = filmes ['1 filme']
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



    
