A Modelagem Dimensional é uma abordagem essencial na construção de Data Warehouses, focalizada na organização dos dados para facilitar sua utilização por meio de ferramentas analíticas, como OLAP (Processamento Analítico Online). Diversos conceitos e tecnologias giram em torno da criação de silos de dados para abordar questões estratégicas de negócios. No entanto, neste contexto, serão apresentados conceitos fundamentais, independentemente das tecnologias específicas.

### Granularidade

A granularidade dos dados em um modelo dimensional reflete o que cada fato representa. Em sistemas transacionais (OLTP), os dados são armazenados em níveis atômicos para garantir a precisão das transações comerciais. No entanto, ao analisar os dados de forma analítica, pode ser necessário agregá-los em níveis mais altos de granularidade para responder a perguntas específicas. A escolha do nível de granularidade afeta diretamente o custo e a velocidade das consultas, sendo fundamental para o sucesso do projeto de análise de dados.

### Modelagem Dimensional

Um sistema orientado à recuperação de dados que suporta grande volume de consultas.

#### Elementos da Modelagem Dimensional

- **Fatos**: Registros que representam medidas derivadas dos eventos de negócios, associados ao nível de granularidade estabelecido. A tabela de fatos sintetiza o relacionamento entre diversas dimensões.

- **Dimensões**: Tabelas que fornecem contexto descritivo aos eventos de negócio. São utilizadas para filtrar e agrupar fatos, permitindo a análise sob diferentes perspectivas.

- **Métricas**: Quantificações atribuídas a registros de fato, geralmente associadas a funções agregadoras. Podem ser aditivas, não aditivas ou semi-aditivas, dependendo da forma como são sumarizadas.

#### Operações OLAP em Cubos

- **Segmentar (Slice)**: Seleciona uma única dimensão do cubo OLAP, criando um novo subcubo.
- **Dividir (Dice)**: Retorna um subcubo selecionando duas ou mais dimensões.
- **Aumentar/Diminuir o Foco (Drill-Down/Roll-Up)**: Navega entre níveis de dados, indo de resumidos a detalhados (Drill-Down) ou de detalhados a resumidos (Roll-Up).
- **Fazer o Pivô (Pivot)**: Modifica a orientação dimensional de um relatório ou consulta.
- **Representação de Dados (Tipos de Modelos)**: Inclui o Esquema em Estrela (Star Schema) e o Esquema em Floco de Neve (Snowflake Schema), cada um com suas características e benefícios específicos.

### Técnicas de Modelagem Dimensional

Transformar um modelo relacional (OLTP) em dimensional envolve a identificação e organização de dimensões e fatos, como exemplificado nos diagramas apresentados.

A Modelagem Dimensional é uma ferramenta poderosa para transformar dados brutos em insights acionáveis, facilitando a análise e a tomada de decisões estratégicas nos negócios.