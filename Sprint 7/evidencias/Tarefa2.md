**Perguntas desta Tarefa**

1. Nesta atividade, faremos uso da imagem `jupyter/all-spark-notebook` ([jupyter/all-spark-notebook](https://registry.hub.docker.com/r/jupyter/all-spark-notebook)) para criar um container e utilizar o recurso de shell oferecido pelo Spark. Os passos a serem executados são:

   1.1 - Realizar o pull da imagem `jupyter/all-spark-notebook`.

   ```bash
   $ docker pull jupyter/all-spark-notebook
   ```
   <img src="pull.png" alt="Texto Alternativo" width="800">  

   1.2 - Criar um container a partir da imagem.

   ```bash
   $ docker run -it -p 8888:8888 jupyter/all-spark-notebook
   ```
   <img src="container.png" alt="Texto Alternativo" width="800">

   <img src="server.png" alt="Texto Alternativo" width="800">

   1.3 - Em outro terminal, execute o comando `pyspark` no seu container. Pesquise sobre o comando `docker exec` para realizar esta ação. Utilize as flags `-i` e `-t` no comando.

   ```bash
   $ docker exec -it 9a1c9f8e76b5 pyspark
   ```
   <img src="spark.png" alt="Texto Alternativo" width="800">


2. Usando o Spark Shell, apresente a sequência de comandos Spark necessários para contar a quantidade de ocorrências de cada palavra contida no arquivo `README.md` de seu repositório Git.

```bash
$ docker cp README.md 9a1c9f8e76b5:/home/jovyan
```
<img src="copy.png" alt="Texto Alternativo" width="800">

- [WordCount.py](WordCount.py)

```python
from pyspark.sql import SparkSession

# Inicia a sessão Spark
spark = SparkSession.builder.appName('WordCount').getOrCreate()

# Lê o arquivo README.md
arquivo = spark.read.text("/home/jovyan/README.md")

# Filtra linhas em branco
arquivo_limpo = arquivo.filter("trim(value) != ''")

# Divide as linhas em palavras, converte para minúsculas e conta a frequência
contagem = (
    arquivo_limpo
    .selectExpr("explode(split(lower(trim(value)), ' ')) as palavra")
    .groupBy("palavra")
    .count()
)

# Ordena e exibe os resultados
ordenado = contagem.orderBy("count", ascending=False)

# Coleta os resultados
resultados = ordenado.collect()

# Salva os resultados em um arquivo de texto
with open("output.txt", "w") as file:
    for resultado in resultados:
        file.write(str(resultado) + "\n")

# Encerra a sessão Spark
spark.stop()
```
<img src="notebook.png" alt="Texto Alternativo" width="800">

<img src="resultado.png" alt="Texto Alternativo" width="800">


- [output.txt](output.txt)

<img src="terminal.png" alt="Texto Alternativo" width="800">




