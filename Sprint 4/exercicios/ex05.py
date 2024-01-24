'''
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, 
acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão
O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
round, map, sorted
'''

import csv

def processa_estudantes():
    
    with open('estudantes.csv', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        resultados = []
        for linha in leitor_csv:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            tres_maiores_notas = sorted(notas, reverse=True)[:3]
            media_tres_maiores = round(sum(tres_maiores_notas) / 3, 2)
            
            resultados.append((nome, tres_maiores_notas, media_tres_maiores))

        resultados_ordenados = sorted(resultados, key=lambda x: x[0])

        for resultado in resultados_ordenados:
            print(f"Nome: {resultado[0]} Notas: {resultado[1]} Média: {resultado[2]}")

processa_estudantes()
