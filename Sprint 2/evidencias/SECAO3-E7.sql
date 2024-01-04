INSERT INTO "select aut.nome
from autor as aut
full join livro as liv 
on aut.codautor = liv.autor  
GROUP  by codautor 
having count(liv.autor) = 0" (nome) VALUES
	 ('ABUNAHMAN, Sérgio Antonio'),
	 ('ALLINGER, Norman L (et al)'),
	 ('ALMEIDA, Alfredo Wagner Berno De'),
	 ('ALMEIDA, Salvador Luiz De'),
	 ('BABBITT, Harold E'),
	 ('BALBO, José Tadeu'),
	 ('BARBOSA, Estêvão José Da Silva'),
	 ('BARROS, Maria Vitória Martins');
