**Descritivo do Desafio**

**Objetivo:**
A minha proposta para este desafio é elaborar um Top 100 filmes da América do Sul, considerando a representação proporcional de cada país nesta lista. Em outras palavras, busco medir a popularidade das produções cinematográficas dos países sul-americanos nos últimos 10 anos, focando em filmes do gênero drama.

**Endpoints Utilizados:**
- Para obter os IDs externos do filme:
```python
url_external_ids = f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids?api_key={API_KEY}&language=pt-BR"
```
- Para obter os detalhes do filme:
```python
url_movie_details = f"https://api.themoviedb.org/3/movie/{imdb_id}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id"
```

**Processo de Elaboração:**
Inicialmente, utilizei a biblioteca `boto3` para carregar o CSV contendo informações sobre filmes do IMDb armazenado no S3. Ao analisar os dados, observei que estavam agrupados por atores, o que não era relevante para o objetivo do desafio. Portanto, optei por eliminar colunas repetidas e trabalhar apenas com os IDs dos filmes.

Em seguida, filtrei os filmes do gênero drama, focando nos últimos 10 anos. Isso reduziu o escopo e tornou os dados mais relevantes para a análise. Com a lista de filmes filtrados, fiz chamadas à API do TMDb para obter os IDs externos de cada filme. Esses IDs foram necessários para obter os detalhes completos dos filmes por meio de outra chamada à API.

Para otimizar o processo e lidar com o grande volume de dados, dividi o CSV em lotes de 5000 linhas. A cada iteração, processava-se um lote de dados, fazendo chamadas à API e gravando os resultados em JSON no bucket S3 da AWS.

Durante o processo, enfrentei desafios devido à lentidão das chamadas à API e ao limite de tempo do Lambda. Algumas IDs não retornaram resultados, o que resultou na perda de cerca de 16,5% dos dados durante a conversão da base IMDB para TMDB. Optei por não tratar esse problema, mantendo o foco na análise dos dados disponíveis.

- [Teste Arquivos json](/DESAFIO/etapa-2/evidencias/output_lambda/teste.ipynb)