import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql.window import Window

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_MOVIES', 'S3_INPUT_TMDB', 'S3_TARGET_FILMES', 'S3_TARGET_POPULARIDADE', 'S3_TARGET_OUTROS', 'S3_TARGET_FINANCEIRO'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_movies = args['S3_INPUT_MOVIES']
source_tmdb = args['S3_INPUT_TMDB']
destino_filmes = args['S3_TARGET_FILMES']
destino_popularidade = args['S3_TARGET_POPULARIDADE']
destino_outros = args['S3_TARGET_OUTROS']
destino_financeiro = args['S3_TARGET_FINANCEIRO']

csv = spark.read.parquet(source_movies)
json = spark.read.parquet(source_tmdb)

csv = csv.filter(csv["genero"].contains("Drama") & (csv["anoLancamento"] >= 2000))

json = json.withColumn("genre_names", expr("transform(genres, x -> x.name)"))

json = json.filter(array_contains(json["genre_names"], "Drama") & (year("release_date") >= 2000))

joined_df = json.join(csv, json["imdb_id"] == csv["id"], "inner")

filmes = joined_df.select(
    json["imdb_id"].alias("id"),
    csv["tituloPrincipal"].alias("tituloCSV"),
    json["production_countries"].alias("origem"),
    json["release_date"].alias("lancamento"),
    json["title"].alias("tituloJSON"),
)
popularidade = joined_df.select(
    json["imdb_id"].alias("id"),
    csv["notaMedia"].alias("notaIMDB"),
    csv["numeroVotos"].alias("votosIMDB"),
    json["vote_average"].alias("notaTMDB"),
    json["vote_count"].alias("votosTMDB"),
)

financeiro = joined_df.select(
    json["imdb_id"].alias("id"),
    json["budget"].alias("orcamento"),
    json["revenue"].alias("receita"),
)

outros = joined_df.select(
    json["imdb_id"].alias("id"),
    json["genres"].alias("genero"),
    json["original_language"].alias("idioma"),
    json["overview"].alias("resumo"),
    json["popularity"].alias("popularidade"),
    json["runtime"].alias("duracao"),
    json["status"].alias("situacao"),
)

filmes = filmes.coalesce(1)
popularidade = popularidade.coalesce(1)
financeiro = financeiro.coalesce(1)
outros = outros.coalesce(1)

filmes.write.format("parquet").mode("overwrite").option("path", destino_filmes).saveAsTable("meubanco.fato_filme")
popularidade.write.format("parquet").mode("overwrite").option("path", destino_popularidade).saveAsTable("meubanco.dim_popularidade")
financeiro.write.format("parquet").mode("overwrite").option("path", destino_financeiro).saveAsTable("meubanco.dim_financeiro")
outros.write.format("parquet").mode("overwrite").option("path", destino_outros).saveAsTable("meubanco.dim_outros")

job.commit()
