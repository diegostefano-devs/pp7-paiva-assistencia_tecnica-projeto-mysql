# PP7 - Sistema Gerenciador - Assistencia Técnica

Sistema desktop para gerenciamento de uma assistência técnica, desenvolvido em **Python** com interface gráfica em **CustomTkinter** e banco de dados **MySQL**. Permite controlar clientes, técnicos, estoque de peças e ordens de serviço, incluindo as peças usadas  para cada atendimento.

## Funcionalidades

- **Clientes:** cadastro com CPF (único), nome e telefone
- **Técnicos:** cadastro com CPF (único), nome e telefone
- **Peças:** controle de estoque com nome, categoria, quantidade, estado e preço
- **Ordens de serviço:** registro do aparelho, do problema relatado, do cliente e do técnico responsável, com acompanhamento de status (padrão: `AGUARDANDO ORÇAMENTO`), valor fixo e valor total
- **Itens da ordem:** peças do estoque utilizadas em cada OS, com quantidade e preço unitário no momento do uso

## Tecnologias

- Python 3
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): interface gráfica
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/): conexão com o MySQL
- MySQL: banco de dados relacional

## Arquitetura

O projeto é organizado em camadas, separando interface, regras de negócio e acesso a dados:

```
pp7-paiva-assistencia_tecnica-projeto-mysql/
├── controllers/          # Regras de negócio, ligam as views aos repositories
├── database/
│   └── conexao.py        # Conexão com o MySQL
├── models/               # Entidades do sistema
│   ├── cliente_model.py
│   ├── tecnico_models.py
│   ├── peca_model.py
│   ├── ordens_model.py
│   └── intes_ordens_model.py
├── repositories/         # Acesso ao banco (consultas SQL)
│   ├── cliente_repository.py
│   ├── tecnico_repositories.py
│   ├── peca_repository.py
│   ├── ordens_repository.py
│   └── itens_ordens_repository.py
├── views/                # Telas da aplicação
│   ├── main_view.py
│   ├── cliente_view/
│   ├── tecnico_view/
│   ├── peca_view/
│   └── ordens_view/
├── banco.sql             # Criação do banco e das tabelas
├── main.py               # Ponto de entrada
└── requirements.txt      # Dependências
```

## Pré-requisitos

- [Python 3](https://www.python.org/downloads/) com `pip`
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- Git

## Instalação e execução

1. **Clone o repositório**
   ```bash
   git clone https://github.com/diegostefano-devs/pp7-paiva-assistencia_tecnica-projeto-mysql.git
   cd pp7-paiva-assistencia_tecnica-projeto-mysql
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/macOS
   source .venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o banco de dados**

   Com o MySQL em execução, rode o script:
   ```bash
   mysql -u root -p < banco.sql
   ```
   Ou abra o `banco.sql` no MySQL Workbench e execute-o.

5. **Configure a conexão**

   Ajuste usuário e senha do MySQL em `database/conexao.py`:
   ```python
   host="localhost"
   user="seu_usuario"
   password="sua_senha"
   database="assistencia_tecnica"
   ```
   > [Adapte este trecho ao formato real do seu `conexao.py`.]

6. **Execute a aplicação**
   ```bash
   python main.py
   ```

## Autores

GitHub: [@diegostefano-devs](https://github.com/diegostefano-devs)
GitHub: [raulsouza220279] (https://github.com/raulsouza220279)
GitHub: [loranahs-source] (https://github.com/loranahs-source)
GitHub: [yansouzays] (https://github.com/yansouzays)

