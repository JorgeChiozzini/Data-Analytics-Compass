-- Criação da tabela tb_pais para armazenar os países.
CREATE TABLE tb_pais (
    idPais INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomePais VARCHAR(40) UNIQUE 
);

-- Inserção do país "Brasil" na tabela tb_pais.
INSERT INTO tb_pais (nomePais) VALUES ('Brasil');

-- Criação da tabela tb_estado para armazenar os estados.
CREATE TABLE tb_estado (
    idEstado INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomeEstado VARCHAR(40), 
    idPais INT, 
    FOREIGN KEY (idPais) REFERENCES tb_pais(idPais) 
);

-- Inserção dos estados na tabela tb_estado, relacionando-os com o país "Brasil".
INSERT INTO tb_estado (nomeEstado, idPais) 
SELECT DISTINCT estadoCliente, 1 FROM tb_locacao; 

-- Criação da tabela tb_cidade para armazenar as cidades.
CREATE TABLE tb_cidade (
    idCidade INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomeCidade VARCHAR(40), 
    idEstado INT, 
    FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado) 
);

-- Inserção das cidades na tabela tb_cidade, relacionando-as com os estados correspondentes.
INSERT INTO tb_cidade (nomeCidade, idEstado) 
SELECT DISTINCT l.cidadeCliente, e.idEstado 
FROM tb_locacao AS l
INNER JOIN tb_estado AS e
	ON l.estadoCliente = e.nomeEstado;

-- Criação da tabela tb_cliente para armazenar os clientes.
CREATE TABLE tb_cliente (
    idCliente INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomeCliente VARCHAR(100), 
    idCidade INT, 
    FOREIGN KEY (idCidade) REFERENCES tb_cidade(idCidade) 
);

-- Inserção dos clientes na tabela tb_cliente, relacionando-os com as cidades correspondentes.
INSERT INTO tb_cliente (idCliente, nomeCliente , idCidade) 
SELECT DISTINCT l.idCliente, l.nomeCliente, c.idCidade
FROM tb_locacao AS l 
INNER JOIN tb_cidade AS c
	ON l.cidadeCliente  = c.nomeCidade;

-- Criação da tabela tb_vendedor para armazenar os vendedores.
CREATE TABLE tb_vendedor (
    idVendedor INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1), 
    idEstado INT, 
    FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado) 
);

-- Inserção dos vendedores na tabela tb_vendedor, relacionando-os com os estados correspondentes.
INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, idEstado) 
SELECT DISTINCT l.idVendedor, l.nomeVendedor, l.sexoVendedor, e.idEstado
FROM tb_locacao AS l
INNER JOIN tb_estado AS e
	ON l.estadoVendedor = e.nomeEstado;

-- Criação da tabela tb_marcaCarro para armazenar as marcas de carro.
CREATE TABLE tb_marcaCarro (
    idMarca INTEGER PRIMARY KEY AUTOINCREMENT, 
    nomeMarca VARCHAR(80) UNIQUE 
);

-- Inserção das marcas de carro na tabela tb_marcaCarro.
INSERT INTO tb_marcaCarro (nomeMarca) 
SELECT DISTINCT l.marcaCarro 
FROM tb_locacao AS l;

-- Criação da tabela tb_modeloCarro para armazenar os modelos de carro.
CREATE TABLE tb_modeloCarro (
    idModelo INTEGER PRIMARY KEY AUTOINCREMENT, 
    idMarca INT, 
    nomeModelo VARCHAR(80), 
    FOREIGN KEY (idMarca) REFERENCES tb_marcaCarro(idMarca) 
);

-- Inserção dos modelos de carro na tabela tb_modeloCarro, relacionando-os com as marcas correspondentes.
INSERT INTO tb_modeloCarro (idMarca, nomeModelo) 
SELECT DISTINCT m.idMarca, l.modeloCarro
FROM tb_locacao AS l
INNER JOIN tb_marcaCarro AS m
	ON l.marcaCarro = m.nomeMarca;

-- Criação da tabela tb_combustivel para armazenar os tipos de combustível.
CREATE TABLE tb_combustivel (
    idCombustivel INTEGER PRIMARY KEY, 
    tipoCombustivel VARCHAR(20) 
);

-- Inserção dos tipos de combustível na tabela tb_combustivel.
INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel FROM tb_locacao; 

-- Criação da tabela tb_carro para armazenar os carros.
CREATE TABLE tb_carro (
    idCarro INTEGER PRIMARY KEY, 
    classiCarro VARCHAR(50), 
    idModelo INT, 
    anoCarro INT, 
    idCombustivel INT, 
    FOREIGN KEY (idModelo) REFERENCES tb_modeloCarro(idModelo), 
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel) 
);

-- Inserção dos carros na tabela tb_carro, relacionando-os com os modelos e tipos de combustível correspondentes.
INSERT INTO tb_carro (idCarro, classiCarro, idModelo, anoCarro, idCombustivel)
SELECT DISTINCT l.idCarro, l.classiCarro, m.idModelo, l.anoCarro, l.idCombustivel
FROM tb_locacao AS l
INNER JOIN tb_modeloCarro AS m 
	ON l.modeloCarro = m.nomeModelo;

-- Criação da tabela tb_locacao_temp para armazenar temporariamente os dados de locação.
CREATE TABLE tb_locacao_temp (
    idLocacao INTEGER PRIMARY KEY AUTOINCREMENT, 
    idCliente INT, 
    idCarro INT, 
    kmCarro INT, 
    dataLocacao DATE, 
    horaLocacao TIME, 
    vlrDiaria DECIMAL(18,2), 
    dataEntrega DATE, 
    horaEntrega TIME, 
    idVendedor INT, 
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente), 
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro), 
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor) 
);

-- Inserção dos dados de locação na tabela tb_locacao_temp.
INSERT INTO tb_locacao_temp (idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT DISTINCT idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

-- Remoção da tabela original tb_locacao.
DROP TABLE tb_locacao;

-- Alteração do nome da tabela temporária para tb_locacao.
ALTER TABLE tb_locacao_temp RENAME TO tb_locacao;

-- Atualização do sexo dos vendedores para seguir uma convenção padronizada ('M' para masculino e 'F' para feminino).
UPDATE tb_vendedor SET sexoVendedor = 
CASE
    WHEN sexoVendedor = '0' THEN 'F'
    WHEN sexoVendedor = '1' THEN 'M'
END;

-- Remoção de vírgulas das datas de locação.
UPDATE tb_locacao  SET dataLocacao = REPLACE(dataLocacao, ',', '');
-- Remoção de vírgulas das datas de entrega.
UPDATE tb_locacao  SET dataEntrega = REPLACE(dataEntrega, ',', '');

-- Conversão do formato de data para 'YYYY-MM-DD' nas datas de locação.
UPDATE tb_locacao  SET dataLocacao = strftime('%Y-%m-%d', substr(dataLocacao,1,4)||'-'||substr(dataLocacao,5,2)||'-'||substr(dataLocacao,7,2));
-- Conversão do formato de data para 'YYYY-MM-DD' nas datas de entrega.
UPDATE tb_locacao  SET dataEntrega = strftime('%Y-%m-%d', substr(dataEntrega,1,4)||'-'||substr(dataEntrega,5,2)||'-'||substr(dataEntrega,7,2));
