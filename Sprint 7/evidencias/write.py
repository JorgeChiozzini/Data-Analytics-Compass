import sys
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import upper
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


df = df.toDF().selectExpr('*', 'upper(nome) as nome')

resp = DynamicFrame.fromDF(df, glueContext, "resp")

glueContext.write_dynamic_frame.from_options(
    frame = resp,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "json")

job.commit()
