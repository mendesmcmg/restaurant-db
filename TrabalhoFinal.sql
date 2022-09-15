drop database if exists trabalhofinal;
create database trabalhofinal;
use trabalhofinal;

-- criação das tabelas

CREATE TABLE Estoque(
	codEstoque int primary key auto_increment unique,
    nome varchar(50) not null
);

CREATE TABLE Restaurante(
    codRest int primary key auto_increment unique,
    nome varchar(45) not null,
    telefone varchar(12) not null,
    endereco varchar(150) not null,
    foto blob,
    Estoque_codEstoque int
);

ALTER TABLE Restaurante
	ADD FOREIGN KEY (Estoque_codEstoque) REFERENCES Estoque(codEstoque);

CREATE TABLE Funcionario(
	codFunc int primary key auto_increment unique,
    cargo varchar(45) not null,
    nome varchar(45) not null,
    salario float not null,
    Restaurante_codRest int
);

ALTER TABLE Funcionario
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES Restaurante(codRest);

CREATE TABLE Mesa(
	codMesa int primary key auto_increment unique,
    Restaurante_codRest int,
    Funcionario_codFunc int
);

ALTER TABLE Mesa
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES Restaurante(codRest);
ALTER TABLE Mesa
	ADD FOREIGN KEY (Funcionario_codFunc) REFERENCES Funcionario(codFunc);

CREATE TABLE Conta(
	codConta int primary key auto_increment unique,
    pagamento boolean not null,
    valor float not null,
    Mesa_codMesa int
);

ALTER TABLE Conta
	ADD FOREIGN KEY (Mesa_codMesa) REFERENCES Mesa(codMesa);

CREATE TABLE Prato(
	codPrato int primary key auto_increment unique,
    nome varchar(45) not null,
    descricao varchar(150),
    valor float not null
);


CREATE TABLE Conta_Prato (
    Conta_codConta int,
    Prato_codPrato int,
    CONSTRAINT Conta_Prato_prato foreign key (Prato_codPrato) references Prato(codPrato),
    CONSTRAINT Conta_Prato_conta foreign key (Conta_codConta) references Conta(codConta),
    CONSTRAINT Conta_Prato_unique UNIQUE (Prato_codPrato, Conta_codConta)
);

CREATE TABLE Restaurante_Prato (
    Restaurante_codRest int,
    Prato_codPrato int,
    CONSTRAINT Restaurante_Prato_prato foreign key (Prato_codPrato) references Prato(codPrato),
    CONSTRAINT Restaurante_Prato_rest foreign key (Restaurante_codRest) references Restaurante(codRest),
    CONSTRAINT Restaurante_Prato_unique UNIQUE (Prato_codPrato, Restaurante_codRest)
);

CREATE TABLE Categoria (
	codCat int primary key auto_increment unique,
    nome varchar(45) not null
);

CREATE TABLE Restaurante_Categoria (
    Restaurante_codRest int,
    Categoria_codCat int,
    CONSTRAINT Restaurante_Categoria_cat foreign key (Categoria_codCat) references Categoria(codCat),
    CONSTRAINT Restaurante_Categoria_rest foreign key (Restaurante_codRest) references Restaurante(codRest),
    CONSTRAINT Restaurante_Categoria_unique UNIQUE (Categoria_codCat, Restaurante_codRest)
);

CREATE TABLE Fornecedor(
	codForn int primary key auto_increment unique,
    nome varchar(45) not null,
    telefone varchar(12) not null,
    Restaurante_codRest int
);

ALTER TABLE Fornecedor
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES  Restaurante(codRest);
    
CREATE TABLE Produto(
	codProd int primary key auto_increment unique,
    nome varchar(45) not null,
    valor float not null
);

CREATE TABLE Fornecedor_Produto (
    Fornecedor_codForn int,
    Produto_codProd int,
    CONSTRAINT Fornecedor_Produto_prod foreign key (Produto_codProd) references Produto(codProd),
    CONSTRAINT Fornecedor_Produto_forn foreign key (Fornecedor_codForn) references Fornecedor(codForn),
    CONSTRAINT Fornecedor_Produto_unique UNIQUE (Produto_codProd, Fornecedor_codForn)
);

CREATE TABLE Estoque_Produto (
    Estoque_codEstoque int,
    Produto_codProd int,
    quantidade int,
    CONSTRAINT Estoque_Produto_prod foreign key (Produto_codProd) references Produto(codProd),
    CONSTRAINT Estoque_Produto_estoque foreign key (Estoque_codEstoque) references Estoque(codEstoque),
    CONSTRAINT Estoque_Produto_unique UNIQUE (Produto_codProd, Estoque_codEstoque)
);

-- inserindo os registros

insert into Estoque (nome) values('Estoque do McDonalds');
insert into Estoque (nome) values('Estoque do China in Box');
insert into Estoque (nome) values('Estoque do Nazo');
insert into Estoque (nome) values('Estoque do Subway');
insert into Estoque (nome) values('Estoque do Dona Lenha');

insert into Restaurante (nome, telefone, endereco, foto, Estoque_codEstoque) values('McDonalds', '1111-1111', 'Endereço 1', null, 1);
insert into Restaurante (nome, telefone, endereco, foto, Estoque_codEstoque) values('China in Box', '2222-2222', 'Endereço 2', null, 2);
insert into Restaurante (nome, telefone, endereco, foto, Estoque_codEstoque) values('Nazo', '3333-3333', 'Endereço 3', null, 3);
insert into Restaurante (nome, telefone, endereco, foto, Estoque_codEstoque) values('Subway', '4444-4444', 'Endereço 4', null, 4);
insert into Restaurante (nome, telefone, endereco, foto, Estoque_codEstoque) values('Dona Lenha', '5555-5555', 'Endereço 5', null, 5);

insert into Funcionario (cargo, nome, salario, Restaurante_codRest) values ('Atendente', 'Luis', 901.00, 1);
insert into Funcionario (cargo, nome, salario, Restaurante_codRest) values ('Atendente', 'Fernando', 902.00, 2);
insert into Funcionario (cargo, nome, salario, Restaurante_codRest) values ('Gerente', 'Maria', 2003.00, 3);
insert into Funcionario (cargo, nome, salario, Restaurante_codRest) values ('Cozinheira', 'Clara', 2004.99, 4);
insert into Funcionario (cargo, nome, salario, Restaurante_codRest) values ('Assistente de Cozinha', 'Carlos', 1205.89, 5);

insert into Mesa (Restaurante_codRest, Funcionario_codFunc) values (1, 1);
insert into Mesa (Restaurante_codRest, Funcionario_codFunc) values (2, 2);
insert into Mesa (Restaurante_codRest, Funcionario_codFunc) values (3, 3);
insert into Mesa (Restaurante_codRest, Funcionario_codFunc) values (4, 4);
insert into Mesa (Restaurante_codRest, Funcionario_codFunc) values (5, 5);

insert into Conta (pagamento, valor, Mesa_codMesa) values (false, 20.00, 1);
insert into Conta (pagamento, valor, Mesa_codMesa) values (true, 30.00, 2);
insert into Conta (pagamento, valor, Mesa_codMesa) values (false, 50.00, 3);
insert into Conta (pagamento, valor, Mesa_codMesa) values (true, 15.50, 4);
insert into Conta (pagamento, valor, Mesa_codMesa) values (false, 60.00, 5);

insert into Prato (nome, descricao, valor) values ('Big Mac', 'Descrição 1', 20.00);
insert into Prato (nome, descricao, valor) values ('Yakisoba', 'Descrição 2', 30.00);
insert into Prato (nome, descricao, valor) values ('Sushi', 'Descrição 3', 50.00);
insert into Prato (nome, descricao, valor) values ('Sanduiche', 'Descrição 4', 15.50);
insert into Prato (nome, descricao, valor) values ('Lasanha', 'Descrição 5', 60.00);

insert into Conta_Prato (Conta_codConta, Prato_codPrato) values (1, 1);
insert into Conta_Prato (Conta_codConta, Prato_codPrato) values (2, 2);
insert into Conta_Prato (Conta_codConta, Prato_codPrato) values (3, 3);
insert into Conta_Prato (Conta_codConta, Prato_codPrato) values (4, 4);
insert into Conta_Prato (Conta_codConta, Prato_codPrato) values (5, 5);

insert into Restaurante_Prato (Restaurante_codRest, Prato_codPrato) values (1, 1);
insert into Restaurante_Prato (Restaurante_codRest, Prato_codPrato) values (2, 2);
insert into Restaurante_Prato (Restaurante_codRest, Prato_codPrato) values (3, 3);
insert into Restaurante_Prato (Restaurante_codRest, Prato_codPrato) values (4, 4);
insert into Restaurante_Prato (Restaurante_codRest, Prato_codPrato) values (5, 5);

insert into Categoria (nome) value ('Fastfood');
insert into Categoria (nome) value ('Chines');
insert into Categoria (nome) value ('Japones');
insert into Categoria (nome) value ('Fastfood');
insert into Categoria (nome) value ('Comida brasileira');

insert into Restaurante_Categoria (Restaurante_codRest, Categoria_codCat) values (1, 1);
insert into Restaurante_Categoria (Restaurante_codRest, Categoria_codCat) values (2, 2);
insert into Restaurante_Categoria (Restaurante_codRest, Categoria_codCat) values (3, 3);
insert into Restaurante_Categoria (Restaurante_codRest, Categoria_codCat) values (4, 4);
insert into Restaurante_Categoria (Restaurante_codRest, Categoria_codCat) values (5, 5);

insert into Fornecedor(nome, telefone, Restaurante_codRest) values ('Fornecedor 1', 1111-1111, 1);
insert into Fornecedor(nome, telefone, Restaurante_codRest) values ('Fornecedor 2', 2222-2222, 2);
insert into Fornecedor(nome, telefone, Restaurante_codRest) values ('Fornecedor 3', 3333-3333, 3);
insert into Fornecedor(nome, telefone, Restaurante_codRest) values ('Fornecedor 4', 4444-4444, 4);
insert into Fornecedor(nome, telefone, Restaurante_codRest) values ('Fornecedor 5', 5555-5555, 5);

insert into Produto(nome, valor) values ('Produto 1', 10);
insert into Produto(nome, valor) values ('Produto 2', 20);
insert into Produto(nome, valor) values ('Produto 3', 30);
insert into Produto(nome, valor) values ('Produto 4', 40);
insert into Produto(nome, valor) values ('Produto 5', 50);

insert into Fornecedor_Produto (Fornecedor_codForn, Produto_codProd) values (1, 1);
insert into Fornecedor_Produto (Fornecedor_codForn, Produto_codProd) values (2, 2);
insert into Fornecedor_Produto (Fornecedor_codForn, Produto_codProd) values (3, 3);
insert into Fornecedor_Produto (Fornecedor_codForn, Produto_codProd) values (4, 4);
insert into Fornecedor_Produto (Fornecedor_codForn, Produto_codProd) values (5, 5);

insert into Estoque_Produto (Estoque_codEstoque, Produto_codProd, quantidade) values (1, 1, 1);
insert into Estoque_Produto (Estoque_codEstoque, Produto_codProd, quantidade) values (2, 2, 2);
insert into Estoque_Produto (Estoque_codEstoque, Produto_codProd, quantidade) values (3, 3, 3);
insert into Estoque_Produto (Estoque_codEstoque, Produto_codProd, quantidade) values (4, 4, 4);
insert into Estoque_Produto (Estoque_codEstoque, Produto_codProd, quantidade) values (5, 5, 5);
