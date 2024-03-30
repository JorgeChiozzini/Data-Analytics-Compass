import json
import requests
import pandas as pd
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    BUCKET = 'datalake-jorge'
    API_KEY = os.environ['api_key']

    # Lê o CSV com filmes do IMDb armazenado no S3
    objeto_movies = s3_client.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/03/11/movies.csv')
    movies_imdb = pd.read_csv(objeto_movies['Body'], sep='|')

    # Remover valores duplicados da coluna 'id'
    movies_imdb = movies_imdb.drop_duplicates(subset=['id'])

    # Substituir '\\N' por valor vazio na coluna 'genero'
    movies_imdb['genero'] = movies_imdb['genero'].replace('\\N', '')

    # Substituir '\\N' por NaN na coluna 'anoLancamento'
    movies_imdb['anoLancamento'] = movies_imdb['anoLancamento'].replace('\\N', pd.NA)

    # Converter a coluna 'anoLancamento' para o tipo de dados datetime
    movies_imdb['anoLancamento'] = pd.to_datetime(movies_imdb['anoLancamento'], errors='coerce')

    # Filtrar os filmes de Drama lançados nos últimos 3 anos
    ano_atual = datetime.now().year
    filmes_filtrados = movies_imdb[
        (movies_imdb['genero'].str.contains('Drama', regex=True, na=False)) &
        (~movies_imdb['anoLancamento'].isna()) & 
        (movies_imdb['anoLancamento'].dt.year >= ano_atual - 10)
    ]

    # Selecionar as próximas 5000 linhas dos filmes filtrados
    filmes_proximos_5000 = filmes_filtrados.iloc[:5000]

    # Dividir os filmes filtrados em lotes de 100 resultados
    resultados_por_lote = [filmes_proximos_5000[i:i+100] for i in range(0, len(filmes_proximos_5000), 100)]

    # Inicializar contador de arquivos
    arquivo_num = 1

    # Iterar sobre cada lote de resultados
    for lote in resultados_por_lote:
        # Inicializar uma lista para armazenar os resultados de cada lote
        resultados = []

        # Iterar sobre cada filme no lote
        for index, row in lote.iterrows():
            # Obter o ID do filme
            movie_id = row['id']
        
            # Construir a URL da chamada à API para obter os IDs externos do filme
            url_external_ids = f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids?api_key={API_KEY}&language=pt-BR"

            # Fazer a chamada à API para obter os IDs externos do filme
            response_external_ids = requests.get(url_external_ids)
            data_external_ids = response_external_ids.json()

            # Verificar se a chamada foi bem-sucedida
            if response_external_ids.status_code == 200:
                # Verificar se há um ID IMDb retornado
                if 'imdb_id' in data_external_ids:
                    # Obter o ID IMDb do filme
                    imdb_id = data_external_ids['imdb_id']

                    # Construir a URL da chamada à API para obter detalhes do filme
                    url_movie_details = f"https://api.themoviedb.org/3/movie/{imdb_id}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id"

                    # Fazer a chamada à API para obter detalhes do filme
                    response_movie_details = requests.get(url_movie_details)
                    data_movie_details = response_movie_details.json()

                    # Verificar se a chamada foi bem-sucedida
                    if response_movie_details.status_code == 200:
                        # Adicionar os detalhes do filme à lista de resultados
                        resultados.append(data_movie_details)
                    else:
                        print(f"Falha na solicitação para obter detalhes do filme {movie_id}.")
                else:
                    print(f"ID IMDb não encontrado nos IDs externos do filme {movie_id}.")
            else:
                print(f"Falha na solicitação para obter IDs externos do filme {movie_id}. Código de status:", response_external_ids.status_code)

        # Converter os resultados do lote para JSON
        json_data = json.dumps(resultados, indent=4)

        # Formata o nome do arquivo com base na data atual, contador e lote
        data_atual = datetime.now().strftime("%Y/%m/%d")
        file_name = f'Raw/TMDB/JSON/{data_atual}/filmes_{arquivo_num}.json'

        # Enviar o arquivo JSON para o Amazon S3
        s3_client.put_object(Body=json_data, Bucket=BUCKET, Key=file_name)

        print(f"Resultados do lote {arquivo_num} salvos com sucesso no Amazon S3.")

        # Incrementar o contador de arquivos
        arquivo_num += 1

    print("Todos os resultados foram salvos com sucesso no Amazon S3.")
