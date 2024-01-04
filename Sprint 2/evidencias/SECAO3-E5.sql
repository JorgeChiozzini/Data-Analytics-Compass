INSERT INTO "select distinct aut.nome 
from autor as aut
left join livro as liv	
on aut.codautor = liv.autor 
left join editora as edi 
on liv.editora = edi.codeditora 
left join endereco as en	
on edi.endereco = en.codendereco 
where en.estado not in ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
order by aut.nome 
" (nome) VALUES
	 ('ABBASCHIAN,  R'),
	 ('ABE, Jair Minoro'),
	 ('ABREU, Antônio Suárez'),
	 ('ACEVEDO MARIN, Rosa Elizabeth'),
	 ('ALEXANDER, Charles K'),
	 ('ALLEN, P. A'),
	 ('ALMEIDA, Fernando José De'),
	 ('ALTMANN, Wolfgang'),
	 ('ALVARENGA, Beatriz Gonçalves De'),
	 ('ALVES, José Jerônimo De Alencar');
INSERT INTO "select distinct aut.nome 
from autor as aut
left join livro as liv	
on aut.codautor = liv.autor 
left join editora as edi 
on liv.editora = edi.codeditora 
left join endereco as en	
on edi.endereco = en.codendereco 
where en.estado not in ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
order by aut.nome 
" (nome) VALUES
	 ('ALVES, William Pereira'),
	 ('AMADO, Nélia'),
	 ('AMALDI, U'),
	 ('AMARAL, Adriano Benayon Do'),
	 ('AMARAL, Luciano Do'),
	 ('ASTOLFI,  Jean-pierre'),
	 ('BARANENKOV, G. S'),
	 ('BARATA, Ronaldo'),
	 ('BARBALHO, Jader'),
	 ('BARBETTA, Pedro Alberto');
INSERT INTO "select distinct aut.nome 
from autor as aut
left join livro as liv	
on aut.codautor = liv.autor 
left join editora as edi 
on liv.editora = edi.codeditora 
left join endereco as en	
on edi.endereco = en.codendereco 
where en.estado not in ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
order by aut.nome 
" (nome) VALUES
	 ('BARBOSA,  Ruy  Madsen'),
	 ('BARDÁLEZ  HOYOS,  Juan  L'),
	 ('BARISON, Thiago'),
	 ('BARP, Wilson José'),
	 ('BARROS, Regina Mambeli'),
	 ('BARSANO, Paulo Roberto');
