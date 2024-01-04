INSERT INTO "select venda.cdvdd , ven.nmvdd 
from tbvendedor as ven
left join tbvendas as venda 
on ven.cdvdd = venda.cdvdd 
where status = 'Concluído'
group by venda.cdvdd 
order by count(venda.cdvdd) desc LIMIT 1" (cdvdd,nmvdd) VALUES
	 (2,'Vendedor 2  ');
