import sys
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import upper
from pyspark.sql.functions import count, desc
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, desc

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
    "s3", 
    {
        "paths": [source_file]
    },
    "csv",
    {
        "withHeader": True,
        "separator": ","
    }
)

df = df.toDF()

df = df.withColumn("ano", df["ano"].cast("int"))

sum_by_name_sex = (
    df.groupBy("nome", "sexo", "ano")
      .agg(sum("total").alias("total_registracoes"))
)

max_female_name = (
    sum_by_name_sex.filter(df.sexo == "F")
                   .groupBy("nome")
                   .agg(sum("total_registracoes").alias("max_total"))
                   .orderBy(desc("max_total"))
                   .first()
)

max_male_name = (
    sum_by_name_sex.filter(df.sexo == "M")
                 .groupBy("nome")
                 .agg(sum("total_registracoes").alias("max_total"))
                 .orderBy(desc("max_total"))
                 .first()
)

max_female_year = (
    sum_by_name_sex.filter((df.sexo == "F") & (sum_by_name_sex.nome == max_female_name["nome"]))
                   .orderBy(desc("total_registracoes"))
                   .first()["ano"]
)

max_male_year = (
    sum_by_name_sex.filter((df.sexo == "M") & (sum_by_name_sex.nome == max_male_name["nome"]))
                 .orderBy(desc("total_registracoes"))
                 .first()["ano"]
)

print("Nome feminino com mais registros:", max_female_name["nome"],
      "com", max_female_name["max_total"],
      "ano", max_female_year)

print("Nome masculino com mais registros:", max_male_name["nome"],
      "com", max_male_name["max_total"],
      "ano", max_male_year)

job.commit()