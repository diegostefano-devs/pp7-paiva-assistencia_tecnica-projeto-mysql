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

use assistencia_tecnica;
SELECT * FROM tecnicos;
SELECT * FROM clientes;
SELECT * FROM ordens_servico;
SELECT * FROM itens_ordem;
SELECT * FROM pecas;


TRUNCATE TABLE itens_ordem;
TRUNCATE TABLE ordens_servico;
-- ============================
-- 1. CLIENTES
-- ============================

INSERT INTO clientes (cpf, nome, telefone) VALUES
('123.456.789-01', 'Carlos Eduardo', '(74) 99911-2233'),
('234.567.890-12', 'Mariana Souza', '(74) 99822-3344'),
('345.678.901-23', 'João Pedro', '(74) 99733-4455'),
('456.789.012-34', 'Ana Beatriz', '(74) 99644-5566'),
('567.890.123-45', 'Roberto Lima', '(74) 99555-6677'),
('678.901.234-56', 'Fernanda Alves', '(74) 99466-7788');

-- ============================
-- 2. TÉCNICOS
-- ============================

INSERT INTO tecnicos (cpf, nome, telefone) VALUES
('111.222.333-44', 'Marcos Oliveira', '(74) 99900-1111'),
('222.333.444-55', 'Ricardo Santos', '(74) 99800-2222'),
('333.444.555-66', 'Pedro Henrique', '(74) 99700-3333');

-- ============================
-- 3. PEÇAS
-- ============================

INSERT INTO pecas (nome, categoria, quantidade, estado, preco) VALUES
('Memória RAM 8GB DDR4', 'Memória', 10, 'Novo', 150.00),
('SSD 480GB Kingston', 'Armazenamento', 8, 'Novo', 230.00),
('Fonte ATX 500W', 'Alimentação', 5, 'Novo', 180.00),
('HD 1TB Seagate', 'Armazenamento', 4, 'Novo', 250.00),
('Cooler para processador', 'Refrigeração', 12, 'Novo', 45.00),
('Teclado USB', 'Periférico', 7, 'Novo', 65.00),
('Mouse USB', 'Periférico', 15, 'Novo', 35.00),
('Placa de rede PCIe', 'Rede', 3, 'Novo', 90.00);

-- ============================
-- 4. ORDENS DE SERVIÇO
-- ============================

INSERT INTO ordens_servico
(id_cliente, id_tecnico, aparelho, problema, status, valor_fixo, valor_total)
VALUES
(1, 1, 'Notebook Dell', 'Notebook não liga.', 'AGUARDANDO ORÇAMENTO', 0.00, 0.00),

(2, 2, 'Desktop', 'Computador apresentando lentidão.', 'AGUARDANDO APROVAÇÃO', 80.00, 310.00),

(3, 1, 'Notebook Lenovo', 'Equipamento desligando sozinho.', 'EM MANUTENÇÃO', 100.00, 145.00),

(4, 3, 'Desktop', 'Computador não reconhece o HD.', 'CONCLUÍDA', 70.00, 320.00),

(5, 2, 'Notebook Acer', 'Teclado com algumas teclas sem funcionar.', 'EM MANUTENÇÃO', 60.00, 125.00),

(6, 3, 'Desktop', 'Computador não apresenta imagem.', 'AGUARDANDO APROVAÇÃO', 90.00, 90.00);

-- ============================
-- 5. ITENS DAS ORDENS
-- ============================

INSERT INTO itens_ordem (id_os, id_peca, quantidade, preco_uni) VALUES
(2, 2, 1, 230.00),
(3, 5, 1, 45.00),
(4, 4, 1, 250.00),
(5, 6, 1, 65.00);

-- ============================
-- 6. PEÇAS ENCOMENDADAS
-- ============================

INSERT INTO peca_encomendada (id_os, nome, preco) VALUES
(2, 'Adaptador SATA USB', 75.00),
(5, 'Teclado Notebook Acer', 120.00),
(6, 'Placa-mãe compatível', 350.00);




