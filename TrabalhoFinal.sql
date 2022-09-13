drop database trabalhofinal;
create database trabalhofinal;
use trabalhofinal;

CREATE TABLE Estoque(
	codEstoque SERIAL primary key UNIQUE,
    nome varchar(50)
);

CREATE TABLE Restaurante(
    codRest SERIAL primary key UNIQUE,
    nome varchar(45),
    telefone varchar(12),
    endereco varchar(100),
    foto bytea,
    Estoque_codEstoque int
);

ALTER TABLE Restaurante
	ADD FOREIGN KEY (Estoque_codEstoque) REFERENCES Estoque(codEstoque);

CREATE TABLE Funcionario(
	codFunc SERIAL primary key UNIQUE,
    cargo varchar(45),
    nome varchar(45),
    salario int,
    Restaurante_codRest int
);

ALTER TABLE Funcionario
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES Restaurante(codRest);

CREATE TABLE Mesa(
	codMesa SERIAL primary key UNIQUE,
    Restaurante_codRest int,
    Funcionario_codFunc int
);

ALTER TABLE Mesa
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES Restaurante(codRest);
ALTER TABLE Mesa
    ADD FOREIGN KEY (Funcionario_codFunc) REFERENCES Funcionario(codFunc);

CREATE TABLE Conta(
	codConta SERIAL primary key UNIQUE,
    pagamento boolean,
    valor float,
    Mesa_codMesa int
);

ALTER TABLE Conta
	ADD FOREIGN KEY (Mesa_codMesa) REFERENCES Mesa(codMesa);

CREATE TABLE Prato(
	codPrato SERIAL primary key UNIQUE,
    nome varchar(45),
    tipo varchar(45),
    valor float
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
	codCat SERIAL primary key UNIQUE,
    nome varchar(45)
);

CREATE TABLE Restaurante_Categoria (
    Restaurante_codRest int,
    Categoria_codCat int,
    CONSTRAINT Restaurante_Categoria_cat foreign key (Categoria_codCat) references Categoria(codCat),
    CONSTRAINT Restaurante_Categoria_rest foreign key (Restaurante_codRest) references Restaurante(codRest),
    CONSTRAINT Restaurante_Categoria_unique UNIQUE (Categoria_codCat, Restaurante_codRest)
);

CREATE TABLE Fornecedor(
	codForn SERIAL primary key UNIQUE,
    nome varchar(45),
    telefone varchar(45),
    produto varchar(45),
    Restaurante_codRest int
);

ALTER TABLE Fornecedor
	ADD FOREIGN KEY (Restaurante_codRest) REFERENCES  Restaurante(codRest);
    
CREATE TABLE Produto(
	codProd SERIAL primary key UNIQUE,
    nome varchar(45)
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
    CONSTRAINT Estoque_Produto_prod foreign key (Produto_codProd) references Produto(codProd),
    CONSTRAINT Estoque_Produto_estoque foreign key (Estoque_codEstoque) references Estoque(codEstoque),
    CONSTRAINT Estoque_Produto_unique UNIQUE (Produto_codProd, Estoque_codEstoque)
);