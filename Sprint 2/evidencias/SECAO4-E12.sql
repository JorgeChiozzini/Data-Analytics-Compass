INSERT INTO "
select depe.cddep, depe.nmdep, depe.dtnasc, sum(venda.qtd*venda.vrunt) as valor_total_vendas
from tbdependente as depe
join tbvendedor as vende 
on vende.cdvdd = depe.cdvdd 
join tbvendas as venda 
on vende.cdvdd = venda.cdvdd 
where status = 'Concluído'
group by venda.cdvdd 
order by sum(venda.qtd*venda.vrunt) LIMIT 1" (cddep,nmdep,dtnasc,valor_total_vendas) VALUES
	 (6,'Dependente 6','2018-03-02 00:00:00',39100.0);
