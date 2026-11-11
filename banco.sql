CREATE DATABASE assistencia_tecnica
	CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    
USE assistencia_tecnica;

CREATE TABLE IF NOT EXISTS clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);


CREATE TABLE IF NOT EXISTS tecnicos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,
	nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS pecas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    quantidade INT UNSIGNED NOT NULL CHECK (quantidade >= 0),
    estado VARCHAR(10),
    preco DECIMAL (10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS ordens_servico (
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_tecnico INT NOT NULL,
    aparelho VARCHAR(20),
    problema TEXT,
    status VARCHAR(30) DEFAULT 'AGUARDANDO ORÇAMENTO',
    valor_fixo DECIMAL (10, 2) DEFAULT 0.00,
    valor_total DECIMAL (10, 2) DEFAULT 0.00,
    
    CONSTRAINT fk_os_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    CONSTRAINT fk_os_tecnico FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id)
    
);

CREATE TABLE IF NOT EXISTS itens_ordem (
	id_os INT NOT NULL,
    id_peca INT NOT NULL,
    quantidade INT UNSIGNED NOT NULL CHECK (quantidade > 0),
    preco_uni DECIMAL (10, 2) NOT NULL,
    
    CONSTRAINT fk_item_os FOREIGN KEY (id_os) REFERENCES ordens_servico(id),
    CONSTRAINT fk_item_peca FOREIGN KEY (id_peca) REFERENCES pecas(id),
    
    PRIMARY KEY (id_os, id_peca)
);

CREATE TABLE IF NOT EXISTS peca_encomendada (
	id_os INT NOT NULL,
    nome VARCHAR(30) NOT NULL,
    preco DECIMAL (10, 2) NOT NULL,
    
    PRIMARY KEY(id_os, nome),
    CONSTRAINT fk_encomenda_os FOREIGN KEY (id_os) REFERENCES ordens_servico(id)
);







