-- Criação da tabela de dimensão para Cliente
CREATE TABLE dim_cliente AS 
SELECT c.idCliente, c.nomeCliente, ci.nomeCidade, e.nomeEstado, p.nomePais
FROM tb_cliente AS c
INNER JOIN tb_cidade AS ci 
	ON c.idCidade = ci.idCidade 
INNER JOIN tb_estado AS e 
	ON ci.idEstado = e.idEstado 
INNER JOIN tb_pais AS p
	ON e.idPais = p.idPais;
	
-- Criação da tabela de dimensão para Vendedor
CREATE TABLE dim_vendedor AS
SELECT v.idVendedor, v.nomeVendedor, v.sexoVendedor, e.nomeEstado
FROM tb_vendedor AS v
INNER JOIN tb_estado AS e
	ON v.idEstado = e.idEstado;

-- Criação da tabela de dimensão para Carro
CREATE TABLE dim_carro AS
SELECT c.idCarro, c.classiCarro, m.nomeMarca, mo.nomeModelo, c.anoCarro, co.tipoCombustivel
FROM tb_carro AS c
INNER JOIN tb_modeloCarro AS mo 
	ON c.idModelo = mo.idModelo 
INNER JOIN tb_marcaCarro AS m 
	ON mo.idMarca = m.idMarca 
INNER JOIN tb_combustivel AS co 
	ON c.idCombustivel = co.idCombustivel;

-- Criação da tabela de dimensão para Data de Locação
CREATE TABLE dim_dtLocacao AS
SELECT 
	dataLocacao, 
	CAST(strftime('%Y', dataLocacao) AS INT) AS ano,
	CAST(strftime('%m', dataLocacao) AS VARCHAR(10)) AS mes,
	CAST(strftime('%w', dataLocacao) AS SMALLINT) AS semana,
	CAST(strftime('%d', dataLocacao) AS SMALLINT) AS dia,
	horaLocacao AS hora
FROM tb_locacao;

-- Criação da tabela de dimensão para Data de Entrega
CREATE TABLE dim_dtEntrega AS
SELECT 
	dataEntrega, 
	CAST(strftime('%Y', dataEntrega) AS INT) AS ano,
	CAST(strftime('%m', dataEntrega) AS VARCHAR(10)) AS mes,
	CAST(strftime('%w', dataEntrega) AS SMALLINT) AS semana,
	CAST(strftime('%d', dataEntrega) AS SMALLINT) AS dia,
	horaEntrega AS hora
FROM tb_locacao;

-- Criação da tabela de fatos para Locação
CREATE TABLE fato_locacao (
    idLocacao INT, 
    idCliente INT, 
    idCarro INT, 
    kmCarro INT, 
    dataLocacao DATETIME, 
    dataEntrega DATETIME, 
    vlrDiaria DECIMAL(18,2), 
    idVendedor INT,
    CONSTRAINT idCliente FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
    CONSTRAINT idCarro FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
    CONSTRAINT dataLocacao FOREIGN KEY (dataLocacao) REFERENCES dim_dtlocacao(dataLocacao),
    CONSTRAINT dataEntrega FOREIGN KEY (dataEntrega) REFERENCES dim_dtEntrega(dataEntrega),
    CONSTRAINT idVendedor FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor)
);

-- Preenchimento da tabela de fatos Locação
INSERT INTO fato_locacao (idLocacao, idCliente, idCarro, kmCarro, datalocacao, dataEntrega, vlrDiaria, idVendedor)
SELECT idLocacao, idCliente, idCarro, kmCarro, dataLocacao, vlrDiaria, dataEntrega, idVendedor
FROM tb_locacao;
