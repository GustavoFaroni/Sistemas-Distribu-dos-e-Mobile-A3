# Gerenciamento de Veículos - Sistemas Distribuídos

Este projeto consiste em uma aplicação distribuída para o controle de veículos, composta por um backend em Python (Flask), um frontend web e persistência em banco de dados PostgreSQL.

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
*   **Python 3.x** instalado.
*   **PostgreSQL** instalado e rodando.
*   **Postman** (opcional, para testes da API).

### 2. Configuração do Banco de Dados
Crie um banco de dados no seu PostgreSQL local:
```sql
CREATE DATABASE veiculos_db;
```

### 3. Configuração do Ambiente (.env)
Dentro da pasta `backend/`, crie um arquivo chamado `.env` e adicione a sua URL de conexão. Exemplo:
```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/veiculos_db
```
*(Substitua `SUA_SENHA` pela senha do seu usuário `postgres`)*

### 4. Instalação de Dependências
Abra o terminal na raiz do projeto e execute:
```bash
pip install -r backend/requirements.txt
```

### 5. Execução do Backend
Inicie o servidor Flask:
```bash
python backend/app.py
```
O servidor rodará em `http://localhost:5000`. O banco de dados e as tabelas são inicializados automaticamente.

### 6. Acesso ao Frontend
Basta abrir o arquivo `frontend/index.html` em qualquer navegador moderno.

---

## 🛠️ Tecnologias Utilizadas
*   **Backend:** Flask, Flask-SQLAlchemy, Flask-CORS.
*   **Banco de Dados:** PostgreSQL.
*   **Frontend:** HTML5, CSS3, JavaScript (Fetch API).
*   **Testes:** Postman (coleções disponíveis na pasta `/postman` e `/backend`).

