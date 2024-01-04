INSERT INTO "select cdpro , nmcanalvendas, nmpro , sum(qtd) as quantidade_vendas
from tbvendas 
where status = 'Concluído'
group by cdpro, nmcanalvendas 
order by sum(qtd)" (cdpro,nmcanalvendas,nmpro,quantidade_vendas) VALUES
	 (2,'Ecommerce','Produto C',15250),
	 (3,'Ecommerce','Produto E',19730),
	 (4,'Ecommerce','Produto SL',72250),
	 (4,'Matriz','Produto SL',82750),
	 (3,'Matriz','Produto E',86300),
	 (5,'Matriz','Produto CH',120270),
	 (6,'Ecommerce','Produto TN  ',232250),
	 (1,'Ecommerce','Produto A',255700),
	 (2,'Matriz','Produto C',444250),
	 (1,'Matriz','Produto A',1102500);
