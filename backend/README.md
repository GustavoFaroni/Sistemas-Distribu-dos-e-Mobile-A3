# Backend Veículos API

Esta é uma API REST desenvolvida em Flask para o gerenciamento de veículos.

## Pré-requisitos

1. Python 3.x
2. PostgreSQL rodando localmente ou remotamente.

## Configuração

1. Crie um banco de dados no PostgreSQL (ex: `veiculos_db`).
2. Edite o arquivo `.env` com as suas credenciais:
   ```env
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
   ```

## Execução

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie a aplicação:
   ```bash
   python app.py
   ```

A API estará disponível em `http://localhost:5000/api/veiculos`.

## Testes

Importe o arquivo `postman/Veiculos_API.postman_collection.json` no Postman para realizar os testes de CRUD.
