import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import when
from pyspark.sql.types import DateType

## @params: [JOB_NAME]
# Obtém os argumentos passados para o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Spark e o contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de origem e destino dos dados como parâmetros internos do job
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lê os arquivos JSON armazenados no S3
df = spark.read.option("multiline", "true").json(source_file)

# Transforma colunas com string vazias "" em campos nulos
columns = df.columns
for col in columns:
    data_type = dict(df.dtypes)[col]
    if data_type == "string":
        df = df.withColumn(col, when(df[col] == "", None).otherwise(df[col]))

# Transforma a coluna 'release_date' para o tipo data
df = df.withColumn("release_date", df["release_date"].cast(DateType()))

# Remove linhas vazias
df = df.filter(df['id'].isNotNull())

# Particiona em 1 arquivo só
df = df.coalesce(1)

# Salva o arquivo em Parquet
df.write.parquet(target_path)

# Finaliza o job
job.commit()
