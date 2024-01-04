INSERT INTO "select cdcli, nmcli, sum((qtd * vrunt)) as gasto
from tbvendas  
where status = 'Concluído'
group by cdcli
order by sum((qtd * vrunt)) desc limit 1" (cdcli,nmcli,gasto) VALUES
	 (9,'Cliente BCA',1237250);
