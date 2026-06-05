Controle de Estacionamento - A3

Aplicação distribuída para gestão de veículos utilizando **Python (Flask)**, **PostgreSQL** e **Frontend Web (HTML/JS)**.

Passo a Passo para Rodar

### 1. Banco de Dados (PostgreSQL)
* Crie um banco de dados chamado `veiculos_db`.
* No arquivo `backend/.env`, atualize a senha do seu usuário `postgres`:
  ```env
  DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/veiculos_db
  ```

### 2. Backend (API)
Abra o terminal na pasta raiz e execute:
```bash
# Entrar na pasta
cd backend

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor
python app.py
```
> O servidor rodará em `http://localhost:5000`. As tabelas são criadas automaticamente no primeiro acesso.

### 3. Frontend (Interface)
1. Navegue até a pasta `frontend`.
2. Abra o arquivo `index.html` em qualquer navegador.

---

## 🛠️ Tecnologias
* **Backend:** Flask, Flask-SQLAlchemy, Flask-CORS.
* **Banco:** PostgreSQL.
* **Frontend:** HTML5, CSS3, JavaScript.
* **Testes:** Postman (coleção disponível na pasta `/postman`).
