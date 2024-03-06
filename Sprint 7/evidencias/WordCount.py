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