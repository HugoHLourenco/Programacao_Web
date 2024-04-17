CREATE TABLE Hugo_IIItbusuario (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(80),
	CPF CHAR(14),
	email VARCHAR(50),
	senha VARCHAR(30)
)



SELECT * FROM Hugo_IIItbusuario
SELECT nome, CPF FROM Hugo_IIItbusuario
SELECT nome, CPF FROM Hugo_IIItbusuario WHERE nome = 'Hugo'


DESC Hugo_IIItbusuario



DELETE FROM Hugo_IIItbusuario WHERE nome = 'Hugo'



UPDATE Hugo_IIItbusuario SET nome = 'juse', CPF = '987.654.321-12' 
WHERE nome = 'Maria'



DROP TABLE Hugo_IIItbusuario



INSERT INTO Hugo_IIItbusuario (nome, CPF, email, senha)
VALUES ('Hugo', '123.345.456-12', 'hugo@gmail.com', '123456')

INSERT INTO Hugo_IIItbusuario (nome, CPF, email, senha)
VALUES ('JUaozim', '333.125.456-12', 'juanzim@gmail.com', '9876655')

INSERT INTO Hugo_IIItbusuario (nome, CPF, email, senha)
VALUES ('Maria', '987.654.321-12', 'maria@gmail.com', '134689')
