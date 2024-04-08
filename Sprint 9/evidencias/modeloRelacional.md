# Modelagem Relacional

O conceito de Modelagem Relacional se origina da teoria de conjuntos, conhecida como álgebra relacional, que busca simplificar a compreensão e o armazenamento de dados. Esse conceito desvincula a localização e a estrutura dos dados da percepção do usuário, representando-os através de tabelas, onde cada tabela corresponde a uma entidade ou relação, e cada linha representa uma instância dessa entidade, com valores associados a seus atributos.

## Modelo Relacional: Exemplo de Tabela

O Modelo Entidade Relacionamento (MER), proposto por Peter P. Chen, baseia-se na ideia de que o mundo está repleto de entidades com características próprias, que se relacionam entre si. Essa teoria, denominada "A Lei do Mundo", divide-se em três partes fundamentais:

1. **O Mundo está cheio de Coisas**: Qualquer elemento do Universo, real ou imaginário, pode ser considerado uma coisa, podendo ser posteriormente definido como uma entidade.
2. **Que Possuem Características Próprias**: As coisas compartilham características comuns, permitindo que sejam agrupadas em conjuntos específicos. Por exemplo, diferentes conselhos profissionais podem ser agrupados sob o conjunto "Órgão Normalizador".
3. **E Que se Relacionam Entre Si**: As relações entre as coisas são essenciais. Podem ser entre elementos de conjuntos distintos ou do mesmo conjunto, representando formas de comunicação ou interação.

## Objeto de Dados ou Entidade

Uma entidade é a representação genérica de um componente do mundo real, sobre o qual desejamos armazenar informações. Essas entidades podem ser tangíveis ou intangíveis e englobam praticamente todas as informações relevantes para um sistema de informação.

### Exemplo de Entidade: Autor

A classificação das entidades pode ser feita de várias maneiras, sendo comum dividir em:

- Coisas Tangíveis
- Funções
- Eventos ou Ocorrências

## Nomenclatura e Dicionarização

Para garantir a compreensão e clareza do modelo de dados, é essencial uma nomenclatura precisa e objetiva, juntamente com uma definição formal dos elementos. A representação gráfica, por si só, nem sempre é suficiente para transmitir os conceitos adequadamente.

## Atributo

Os atributos são propriedades particulares que descrevem uma entidade, como nome, idade ou endereço. Podem ser classificados em simples, compostos, monovalorados, multivalorados, derivados e chaves.

## Relacionamento

As entidades podem se relacionar entre si, formando associações que são representadas por verbos. Esses relacionamentos têm cardinalidades que indicam o número de ocorrências permitidas em cada extremidade do relacionamento.

## Tipos de Modelos de Dados

Com base nos conceitos acima, os modelos de dados podem ser divididos em três níveis:

1. **Modelo Conceitual**: O mais próximo da realidade dos usuários, desenvolvido a partir dos requisitos do sistema e representado por diagramas de Entidade e Relacionamento ou Diagramas de Classes.
2. **Modelo Lógico**: Descreve como os dados serão armazenados no banco e seus relacionamentos, utilizando alguma tecnologia específica.
3. **Modelo Físico**: Descreve a implementação real da estrutura de armazenamento no banco de dados, escolhendo o Sistema Gerenciador de Banco de Dados (SGBD) adequado.

## Integridade e Normalização

A integridade dos dados é mantida por meio de restrições e normalização, processos que visam evitar anomalias na inclusão, exclusão e alteração de dados, garantindo a estabilidade e a consistência do modelo.

- **Primeira Forma Normal (1FN)**: Elimina atributos repetitivos, garantindo a atomicidade dos dados.
- **Segunda Forma Normal (2FN)**: Elimina dependências parciais, separando valores em tabelas distintas.
- **Terceira Forma Normal (3FN)**: Elimina dependências transitivas, garantindo que todos os campos não-chave dependam diretamente da chave primária.

