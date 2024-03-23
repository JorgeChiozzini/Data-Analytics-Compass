### Perguntas dessa tarefa:

**[Warm up]**  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

**[Warm up]** Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.

**[Laboratório]** Elaborar um código Python para gerar um dataset de nomes de pessoas. Siga os passos a seguir para realizar a atividade:

**Passo 1:**  Instalar biblioteca names para geração de nomes aleatórios. O comando de instalação é `pip install names`

**Passo 2** Importar as bibliotecas `random`, `time`, `os` e `names` em seu código

**Passo 3:** Definir os parâmetros para geração do dataset, ou seja, a quantidades de nomes aleatórios e a quantidade de nomes que devem ser únicos.

Define a semente de aleatoriedade
```python
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000
```

*Nota:* Quando trabalhamos com números randômicos em computação, na realidade, estamos falando de valores pseudoaleatórios, uma vez que o computador não consegue gerar números verdadeiramente aleatórios. No caso do Python, a função `random.seed` inicializa o algoritmo responsável pela geração de valores randômicos. É um processo determinístico, pois os valores gerados serão sempre os mesmos se utilizado a mesma configuração de inicialização. A este número inicial chamamos de semente de aleatoriedade.

**Passo 4:** Gerar os nomes aleatórios.
```python
aux=[]
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados=[]

for i in range(0,qtd_nomes_aleatorios):
    dados.append(random.choice(aux))
```

**Passo 5:** Gerar um arquivo de texto contendo todos os nomes, um a cada linha. O nome do arquivo deve ser `nomes_aleatorios.txt`

**Passo 6:** Abrir o arquivo e verificar seu conteúdo (editor de texto)