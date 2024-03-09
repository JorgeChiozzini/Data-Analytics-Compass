<h1 align="center"> Sprint 7</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#tarefa">Tarefa</a> •
 <a href="#Laboratório">Laboratório</a> •
 <a href="#desafio">Desafio</a>
</p>

<br> 

<a id="sobre"></a>
## 📎  Sobre

### Cursos e certificados
- [Hadoop, MapReduce for Big Data problems](certificados/hadoop.png)
- [Formação Spark com Pyspark](certificados)

### Leitura
- [Arquitetura Lambda, ETL/ELT, Bibliotecas Python NumPy e Pandas](certificados/DA-ETL-Pandas-NumPy.pdf)
- [Apache Hadoop e Apache Spark](certificados/DA-Apache+Hadoop+e+Apache+Spark.pdf)

<br>

<a id="tarefa"></a>
## 📝   tarefa

### Python com Pandas e Numpy
- [actors.csv](evidencias/actors.csv)
- [Tarefa 1 - Resultado](evidencias/Tarefa1.ipynb)

### Apache Spark - Contador de Palavras
- [Tarefa 2 - Resultado](evidencias/Tarefa2.md)
- [output.txt](evidencias/output.txt)

<br>

<a id="Laboratório"></a>
## 👩‍💻 Laboratório

### Lab AWS Glue
- [Lab - Resultado](evidencias/Lab.md)

<br>

<a id="desafio"></a>
## 🎯  Desafio 

### Tarefa: Desafio Parte 1 - ETL


Instruções da tarefa

Ingestão Batch: a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos para a nuvem. Nesse caso utilizaremos, principalmente, as lib boto3 como parte do processo de ingestão via batch para geração de arquivo (CSV).

Perguntas dessa tarefa

1. Implementar código Python:
- ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados
- utilizar a lib boto3 para carregar os dados para a AWS
- acessar a AWS e grava no S3, no bucket definido com RAW Zone
- no momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
Por exemplo:
S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv
S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado

3. Executar localmente o container docker para realizar a carga dos dados ao S3