import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType, StructField
from pyspark.sql.functions import col, when

## @params: [JOB_NAME]
# Obtém os argumentos passados para o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Spark e o contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho de origem e destino dos dados como parâmetros internos do job
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Colunas do CSV
columns = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos"]

# Schema a ser usado no CSV
schema = StructType([
        StructField(columns[0], StringType()),
        StructField(columns[1], StringType()),
        StructField(columns[2], StringType()),
        StructField(columns[3], IntegerType()),
        StructField(columns[4], IntegerType()),
        StructField(columns[5], StringType()),
        StructField(columns[6], FloatType()),
        StructField(columns[7], IntegerType()),
        StructField(columns[8], StringType()),
        StructField(columns[9], StringType()),
        StructField(columns[10], StringType()),
        StructField(columns[11], IntegerType()),
        StructField(columns[12], IntegerType()),
        StructField(columns[13], StringType()),
        StructField(columns[14], StringType())
    ])

# Cria um DataFrame a partir do CSV
df = spark.read.format("csv").option("sep","|").schema(schema).load(source_file)

# Remove a primeira linha que é o cabeçalho com erros do CSV
df = df.filter(df['id'] != 'id')

# Remove filmes duplicados 
df = df.drop_duplicates(subset=['id'])

# Transforma \N em nulos para facilitar a análise
df_nulls = df
for column in columns:
    df_nulls = df_nulls.withColumn(column, when(col(column) == "\\N", None).otherwise(col(column)))

# Junta os dados para ter apenas um arquivo Parquet de saída
df_coalesce = df_nulls.coalesce(1)

# Salva como Parquet no S3
df_coalesce.write.parquet(target_path)

# Finaliza o job
job.commit()
