import json
import aiohttp
import pandas as pd
import boto3
import os
import asyncio
from datetime import datetime

async def fetch_movie_details(session, movie_id, API_KEY):
    async with session.get(f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids?api_key={API_KEY}&language=pt-BR") as response:
        data_external_ids = await response.json()
        if response.status == 200 and 'imdb_id' in data_external_ids:
            imdb_id = data_external_ids['imdb_id']
            async with session.get(f"https://api.themoviedb.org/3/movie/{imdb_id}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id") as response_movie_details:
                data_movie_details = await response_movie_details.json()
                if response_movie_details.status == 200:
                    return data_movie_details
                else:
                    print(f"Failed to get details for movie {movie_id}.")
        else:
            print(f"IMDb ID not found in external IDs for movie {movie_id}.")

async def main():
    s3_client = boto3.client('s3')
    BUCKET = 'datalake-jorge'
    API_KEY = os.environ['api_key']

    objeto_movies = s3_client.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2024/03/11/movies.csv')
    movies_imdb = pd.read_csv(objeto_movies['Body'], sep='|')
    movies_imdb = movies_imdb.drop_duplicates(subset=['id'])
    movies_imdb['genero'] = movies_imdb['genero'].replace('\\N', '')
    movies_imdb['anoLancamento'] = movies_imdb['anoLancamento'].replace('\\N', pd.NA)
    movies_imdb['anoLancamento'] = pd.to_datetime(movies_imdb['anoLancamento'], errors='coerce')

    ano_atual = datetime.now().year
    filmes_filtrados = movies_imdb[
        (movies_imdb['genero'].str.contains('Drama', regex=True, na=False)) &
        (~movies_imdb['anoLancamento'].isna()) & 
        (movies_imdb['anoLancamento'].dt.year >= ano_atual - 10)
    ]

    filmes_proximos_5000 = filmes_filtrados.iloc[25000:30000]
    resultados_por_lote = [filmes_proximos_5000[i:i+100] for i in range(0, len(filmes_proximos_5000), 100)]

    arquivo_num = 1

    async with aiohttp.ClientSession() as session:
        for lote in resultados_por_lote:
            tasks = []
            resultados = []
            for index, row in lote.iterrows():
                tasks.append(fetch_movie_details(session, row['id'], API_KEY))

            for task in asyncio.as_completed(tasks):
                movie_details = await task
                if movie_details:
                    resultados.append(movie_details)

            json_data = json.dumps(resultados, indent=4)
            data_atual = datetime.now().strftime("%Y/%m/%d")
            file_name = f'Raw/TMDB/JSON/{data_atual}/filmes_{arquivo_num}.json'
            s3_client.put_object(Body=json_data, Bucket=BUCKET, Key=file_name)
            print(f"Resultados do lote {arquivo_num} salvos com sucesso no Amazon S3.")
            arquivo_num += 1

    print("Todos os resultados foram salvos com sucesso no Amazon S3.")

def lambda_handler(event, context):
    asyncio.run(main())

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Movies fetched and saved successfully"})
    }


#4 minutos