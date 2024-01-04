INSERT INTO "SELECT COUNT(liv.editora) as quantidade, ed.nome , en.estado, en.cidade
FROM livro as liv
left join editora as ed
on liv.editora = ed.codeditora 
left join endereco as en
on ed.endereco = en.codendereco 
group by editora 
order by COUNT(liv.editora) desc " (quantidade,nome,estado,cidade) VALUES
	 (138,' CBMM','PARANÁ','Guaratuba'),
	 (30,' Ática','SÃO PAULO','São Paulo');