import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Obtém os argumentos passados para o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_MOVIES', 'S3_INPUT_TMDB', 'S3_TARGET_FILME_FATO', 'S3_TARGET_FILME_DIM', 'S3_TARGET_PAISES', 'S3_TARGET_ASSOCIACAO_PAISES'])

# Inicializa o contexto do Spark e o contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define os caminhos de origem e destino dos dados
source_movies = args['S3_INPUT_MOVIES']
source_tmdb = args['S3_INPUT_TMDB']
destino_filmes_fato = args['S3_TARGET_FILME_FATO']
destino_filmes_dim = args['S3_TARGET_FILME_DIM']
destino_paises = args['S3_TARGET_PAISES']
destino_associacao_paises = args['S3_TARGET_ASSOCIACAO_PAISES']

# Lê os dados do S3 em formato parquet
# Lendo os dados de filmes do S3
csv = spark.read.parquet(source_movies)
# Lendo os dados do TMDB do S3
json = spark.read.parquet(source_tmdb)

# Filtra os filmes de drama lançados a partir de 2000
# Filtrando os dados do CSV pelos filmes de drama lançados a partir de 2000
csv = csv.filter(csv["genero"].contains("Drama") & (csv["anoLancamento"] >= 2000))
# Filtrando os dados do JSON pelos filmes de drama lançados a partir de 2000
json = json.withColumn("genre_names", expr("transform(genres, x -> x.name)"))
json = json.filter(array_contains(json["genre_names"], "Drama") & (year("release_date") >= 2000))

# Realiza o join dos dataframes
# Juntando os dataframes CSV e JSON usando o ID do IMDB como chave
joined_df = json.join(csv, json["imdb_id"] == csv["id"], "inner")

# Seleciona as colunas necessárias para os diferentes datasets
# Selecionando as colunas relevantes para a dimensão de filmes
filme_dim = joined_df.select(
    json["imdb_id"].alias("id"),
    csv["tituloPrincipal"].alias("tituloCSV"),
    json["title"].alias("tituloJSON"),
    json["release_date"].alias("lancamento"),
    json["original_language"].alias("idioma"),
    json["overview"].alias("resumo"),
)

# Selecionando as colunas relevantes para a fato de filmes
filme_fato = joined_df.select(
    json["imdb_id"].alias("id"),
    csv["notaMedia"].alias("notaIMDB"),
    csv["numeroVotos"].alias("votosIMDB"),
    json["vote_average"].alias("notaTMDB"),
    json["vote_count"].alias("votosTMDB"),
    json["popularity"].alias("popularidade"),
    json["budget"].alias("orcamento"),
    json["revenue"].alias("receita"),
)

# Explode os países de produção para uma dimensão de países
paises = json.select(explode("production_countries").alias("origem"))
paises_dim = paises.selectExpr(
    "origem.iso_3166_1 as codigo",
    "origem.name as nome"
).distinct()

# Cria uma associação entre filmes e países
paises_exploded = json.select("imdb_id", explode("production_countries.iso_3166_1").alias("codigo_origem"))
associacao_filme_pais = paises_exploded.join(paises_dim, paises_exploded["codigo_origem"] == paises_dim["codigo"], "inner").select("imdb_id", "codigo")
associacao_filme_pais = associacao_filme_pais.withColumnRenamed("imdb_id", "id")

# Coalesce para um único arquivo
filme_fato = filme_fato.coalesce(1)
filme_dim = filme_dim.coalesce(1)
paises_dim = paises_dim.coalesce(1)
associacao_filme_pais = associacao_filme_pais.coalesce(1)

# Salva os datasets como tabelas no formato Parquet no S3
# Salva a dimensão de filmes no S3
filme_fato.write.format("parquet").mode("overwrite").option("path", destino_filmes_fato).saveAsTable("meubanco.fato_filme")
# Salva a fato de filmes no S3
filme_dim.write.format("parquet").mode("overwrite").option("path", destino_filmes_dim).saveAsTable("meubanco.dim_filme")
# Salva a dimensão de países no S3
paises_dim.write.format("parquet").mode("overwrite").option("path", destino_paises).saveAsTable("meubanco.dim_paises")
# Salva a associação entre filmes e países no S3
associacao_filme_pais.write.format("parquet").mode("overwrite").option("path", destino_associacao_paises).saveAsTable("meubanco.associacao_filme_pais")

# Finaliza o job
job.commit()
