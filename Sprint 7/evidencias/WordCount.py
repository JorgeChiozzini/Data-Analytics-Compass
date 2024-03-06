from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, lower, trim, regexp_replace
from pyspark.sql import functions as F

# Inicia a sessão Spark
spark = SparkSession.builder.appName('WordCount').getOrCreate()

# Lê o arquivo README.md
arquivo = spark.read.text("README.md")

# Utiliza Spark SQL para extrair palavras
arquivo.createOrReplaceTempView("arquivo_view")
palavras = spark.sql("""
    SELECT explode(split(lower(trim(regexp_replace(value, '[^a-zA-Z ]', ''))), ' ')) as palavra
    FROM arquivo_view
    WHERE trim(value) != ''
""")

# Filtra linhas em branco
palavras_limpo = palavras.filter("palavra != ''")

# Conta a frequência
contagem = palavras_limpo.groupBy("palavra").count()

# Ordena e exibe os resultados
ordenado = contagem.orderBy("count", ascending=False)

# Coleta os resultados
resultados = ordenado.collect()

# Salva os resultados em um arquivo de texto
with open("output.txt", "w") as file:
    for resultado in resultados:
        file.write(f"{resultado['palavra']}: {resultado['count']}\n")

# Encerra a sessão Spark
spark.stop()