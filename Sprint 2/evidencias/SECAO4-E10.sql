INSERT INTO "select ven.nmvdd as vendedor, sum((qtd * vrunt)) as valor_total_vendas,round(((select sum((qtd * vrunt))) * ven.perccomissao / 100 ),2) as comissao
from tbvendedor as ven
left join tbvendas as venda 
on ven.cdvdd = venda.cdvdd 
where status = 'Concluído'
group by venda.cdvdd 
order by sum((select (qtd * vrunt)) * ven.perccomissao / 100 ) desc" (vendedor,valor_total_vendas,comissao) VALUES
	 ('Vendedor 2  ',2472020.0,24720.2),
	 ('Vendedor 8',1237250,6186.25),
	 ('Vendedor 10',747250,3736.25),
	 ('Vendedor 5',270122.5,1350.61),
	 ('Vendedor 1',121530.0,1215.3),
	 ('Vendedor 3',57630.0,576.3),
	 ('Vendedor 7',69700.0,348.5),
	 ('Vendedor 6  ',50830.0,254.15),
	 ('Vendedor 4',42908.0,214.54),
	 ('Vendedor 9',39100.0,195.5);
