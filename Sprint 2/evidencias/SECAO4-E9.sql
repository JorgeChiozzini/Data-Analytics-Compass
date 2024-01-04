INSERT INTO "select cdpro , nmpro 
from tbvendas 
where status = 'Concluído' and dtven BETWEEN '2014-02-03' and '2018-02-02'
group by cdpro 
order by count(cdpro) desc limit 1" (cdpro,nmpro) VALUES
	 (1,'Produto A');
