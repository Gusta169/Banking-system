Create table clientes(
	id serial primary key,
	nome varchar(100),
	cpf varchar(11) UNIQUE NOT NULL,
	saldo varchar(10,2)default 0,
    senha VARCHAR(255) NOT NULL
);