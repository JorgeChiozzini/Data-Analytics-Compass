INSERT INTO "select aut.codautor, aut.nome, count(liv.autor) as quantidade_publicacoes
from autor as aut
left join livro as liv 
on aut.codautor = liv.autor 
group by autor 
order by count(liv.autor) DESC LIMIT 1" (codautor,nome,quantidade_publicacoes) VALUES
	 (67,'BARP, Wilson José',7);
