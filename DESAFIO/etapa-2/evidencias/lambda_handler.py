import json
import aiohttp
import pandas as pd
import boto3
import os
import asyncio
from datetime import datetime

async def fetch_movie_details(session, movie_id, API_KEY):
    # Busca os detalhes do filme usando a sessão aiohttp
    async with session.get(f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids?api_key={API_KEY}&language=pt-BR") as response:
        data_external_ids = await response.json()
        # Verifica se o ID do IMDb existe nos IDs externos
        if response.status == 200 and 'imdb_id' in data_external_ids:
            imdb_id = data_external_ids['imdb_id']
            # Busca os detalhes do filme usando o ID do IMDb
            async with session.get(f"https://api.themoviedb.org/3/movie/{imdb_id}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id") as response_movie_details:
                data_movie_details = await response_movie_details.json()
                # Verifica se os detalhes do filme foram obtidos com sucesso
                if response_movie_details.status == 200:
                    return data_movie_details
                else:
                    print(f"Falha ao obter detalhes do filme {movie_id}.")
        else:
            print(f"ID do IMDb não encontrado nos IDs externos para o filme {movie_id}.")

async def main():
    # Inicializa o cliente AWS S3
    s3_client = boto3.client('s3')
    BUCKET = 'datalake-jorge'
    API_KEY = os.environ['api_key']

    # Busca dados do filme no AWS S3
    objeto_movies = s3_client.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/03/11/movies.csv')
    movies_imdb = pd.read_csv(objeto_movies['Body'], sep='|')
    movies_imdb = movies_imdb.drop_duplicates(subset=['id'])
    movies_imdb['genero'] = movies_imdb['genero'].replace('\\N', '')
    movies_imdb['anoLancamento'] = movies_imdb['anoLancamento'].replace('\\N', pd.NA)
    movies_imdb['anoLancamento'] = pd.to_datetime(movies_imdb['anoLancamento'], errors='coerce')

    # Filtra os filmes por gênero e ano de lançamento
    filmes_filtrados = movies_imdb[
        (movies_imdb['genero'].str.contains('Drama', regex=True, na=False)) &
        (~movies_imdb['anoLancamento'].isna()) & 
        (movies_imdb['anoLancamento'].dt.year >= 2000)
    ]

    # Seleciona um subconjunto de filmes para processamento
    filmes_proximo_conjunto = filmes_filtrados.iloc[:18000]
    resultados_por_lote = [filmes_proximo_conjunto[i:i+100] for i in range(0, len(filmes_proximo_conjunto), 100)]

    arquivo_num = 1

    async with aiohttp.ClientSession() as session:
        for lote in resultados_por_lote:
            tasks = []
            resultados = []
            # Cria tarefas para buscar os detalhes do filme de forma assíncrona
            for index, row in lote.iterrows():
                tasks.append(fetch_movie_details(session, row['id'], API_KEY))

            # Executa as tarefas de forma assíncrona e coleta os resultados
            for task in asyncio.as_completed(tasks):
                movie_details = await task
                if movie_details:
                    resultados.append(movie_details)

            # Converte os resultados para JSON e armazena no AWS S3
            json_data = json.dumps(resultados, indent=4)
            data_atual = datetime.now().strftime("%Y/%m/%d")
            file_name = f'Raw/TMDB/JSON/{data_atual}/filmes_{arquivo_num}.json'
            s3_client.put_object(Body=json_data, Bucket=BUCKET, Key=file_name)
            print(f"Resultados do lote {arquivo_num} salvos com sucesso no Amazon S3.")
            arquivo_num += 1

    print("Todos os resultados foram salvos com sucesso no Amazon S3.")

def lambda_handler(event, context):
    # Executa a função principal de forma assíncrona
    asyncio.run(main())

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Filmes obtidos e salvos com sucesso"})
    }