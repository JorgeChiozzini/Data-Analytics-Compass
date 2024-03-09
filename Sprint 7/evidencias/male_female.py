import sys
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import upper
from pyspark.sql.functions import count, desc
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

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

sum_by_name_sex = df.groupBy("nome", "sexo").agg({"total": "sum", "ano": "first"})

max_female_name = (sum_by_name_sex.filter(df.sexo == "F")
                                   .orderBy(desc("sum(total)"))
                                   .first())

max_male_name = (sum_by_name_sex.filter(df.sexo == "M")
                                 .orderBy(desc("sum(total)"))
                                 .first())

print("Nome feminino com mais registros:", max_female_name["nome"], "com", max_female_name["sum(total)"], "registros em", max_female_name["first(ano)"])
print("Nome masculino com mais registros:", max_male_name["nome"], "com", max_male_name["sum(total)"], "registros em", max_male_name["first(ano)"])


job.commit()
