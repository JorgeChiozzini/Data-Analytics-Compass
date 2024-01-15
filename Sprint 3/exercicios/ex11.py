'''
Escreva um programa para ler o conteúdo do arquivo 
texto arquivo_texto.txt e imprimir o seu conteúdo.
Dica: leia a documentação da função open(...)
'''

with open('arquivo_texto.txt', 'r') as arquivo:
        conteudo = arquivo.read()

        print(conteudo)
