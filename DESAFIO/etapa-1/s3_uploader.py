import boto3
from datetime import datetime
import os

# Função para carregar dados para o S3
def upload_to_s3(file_path, bucket_name, storage_layer, data_origin, data_format, data_specification):
    s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    region_name='us-east-1'
)

    # Obter a data de processamento
    processing_date = datetime.utcnow().strftime("%Y/%m/%d")

    # Formatar o caminho no S3
    s3_key = f"{storage_layer}/{data_origin}/{data_format}/{data_specification}/{processing_date}/{os.path.basename(file_path)}"

    # Upload do arquivo para o S3
    s3_client.upload_file(file_path, bucket_name, s3_key)
    print(f"Arquivo {file_path} carregado com sucesso para {bucket_name}/{s3_key}")

# Ler os arquivos CSV e carregar para o S3
def load_csv_to_s3(file_path, bucket_name, storage_layer, data_origin, data_format, data_specification):
    upload_to_s3(file_path, bucket_name, storage_layer, data_origin, data_format, data_specification)

# Caminhos dos arquivos CSV
movies_file_path = "dados/movies.csv"
series_file_path = "dados/series.csv"

# Configurações do S3
s3_bucket_name = "datalake-jorge"
s3_storage_layer = "Raw"
s3_data_origin_movies = "Local"
s3_data_origin_series = "Local"
s3_data_format = "CSV"
s3_data_specification = "Movies"
s3_data_specification_series = "Series"

# Carregar dados para o S3
load_csv_to_s3(movies_file_path, s3_bucket_name, s3_storage_layer, s3_data_origin_movies, s3_data_format, s3_data_specification)
load_csv_to_s3(series_file_path, s3_bucket_name, s3_storage_layer, s3_data_origin_series, s3_data_format, s3_data_specification_series)
