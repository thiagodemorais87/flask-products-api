<div align="center">

# 📦 API RESTful de Gerenciamento de Produtos

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-e91e63?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

*API RESTful desenvolvida em Python para gerenciamento completo de produtos, construída com arquitetura em camadas, validação de dados e documentação Swagger/OpenAPI.*

[Visão Geral](#-visão-geral) •
[Arquitetura](#-arquitetura-do-projeto) •
[Estrutura](#-estrutura-de-diretórios) •
[Endpoints](#-endpoints-da-api) •
[Como Executar](#-como-executar) •
[Tratamento de Erros](#-tratamento-de-erros)

</div>

---

# 📌 Visão Geral

Esta aplicação fornece uma API RESTful para gerenciamento de produtos utilizando **Flask**, **SQLAlchemy**, **Pydantic** e **Swagger**.

O projeto foi desenvolvido seguindo princípios de **Clean Code**, **Arquitetura em Camadas** e **Repository Pattern**, promovendo organização, facilidade de manutenção e escalabilidade.

## ✨ Funcionalidades

- ✅ CRUD completo de produtos
- ✅ Validação automática utilizando Pydantic
- ✅ Persistência de dados com SQLAlchemy ORM
- ✅ Documentação interativa com Swagger UI
- ✅ Tratamento global de exceções
- ✅ Arquitetura em camadas
- ✅ Código organizado e de fácil manutenção

---

# 🏗 Arquitetura do Projeto

A aplicação segue uma arquitetura dividida em responsabilidades bem definidas.

```text
          Cliente
(Postman / Swagger / Front-end)
                │
                ▼
      ┌─────────────────────┐
      │ Routes / Blueprints │
      └──────────┬──────────┘
                 │
                 ▼
      ┌─────────────────────┐
      │     Services        │
      └───────┬─────────────┘
              │
      ┌───────┴───────────────┐
      ▼                       ▼
 Pydantic Schemas       Repository Layer
      │                       │
      └──────────────┬────────┘
                     ▼
               SQLAlchemy ORM
                     │
                     ▼
                  Database
```

---

# 📁 Estrutura de Diretórios

```text
flask-products-api/
│
├── app/
│   ├── models/              # Modelos SQLAlchemy
│   ├── repositories/        # Acesso ao banco de dados
│   ├── routes/              # Endpoints HTTP
│   ├── schemas/             # Validação (Pydantic)
│   ├── services/            # Regras de negócio
│   ├── errors.py            # Tratamento global de erros
│   ├── extensions.py        # Inicialização das extensões
│   └── __init__.py          # Factory da aplicação
│
├── instance/                # Banco SQLite
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

# 🛣 Endpoints da API

Todas as respostas seguem o padrão JSON.

| Método | Endpoint | Descrição | Status |
|---------|----------|-----------|--------|
| GET | `/api/products` | Lista todos os produtos | 200 |
| POST | `/api/products` | Cria um novo produto | 201 |
| GET | `/api/products/<id>` | Busca produto por ID | 200 / 404 |
| PUT | `/api/products/<id>` | Atualiza um produto | 200 / 404 |
| DELETE | `/api/products/<id>` | Remove um produto | 200 / 404 |

---

# 📦 Exemplo de Payload

## Criar Produto

**POST** `/api/products`

```json
{
  "name": "Teclado Mecânico RGB",
  "price": 250.00,
  "stock": 15
}
```

---

## Resposta

```json
{
  "data": {
    "id": 1,
    "name": "Teclado Mecânico RGB",
    "price": 250.0,
    "stock": 15
  },
  "message": "Produto criado com sucesso",
  "status": 201
}
```

---

# 🚨 Tratamento de Erros

A API possui tratamento global de exceções.

## Exemplo de erro de validação

```json
{
  "error": "Erro de validação nos dados enviados",
  "details": [
    {
      "loc": ["price"],
      "msg": "Input should be greater than 0",
      "type": "greater_than"
    }
  ],
  "status": 422
}
```

---

# 🚀 Como Executar

## Pré-requisitos

- Python 3.10+
- Git

---

## 1. Clone o repositório

```bash
git clone https://github.com/thiagodemorais87/flask-products-api.git

cd flask-products-api
```

---

## 2. Crie um ambiente virtual

### Windows

```bash
python -m venv venv

.\venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Execute a aplicação

```bash
python run.py
```

A aplicação estará disponível em:

```
http://127.0.0.1:5000
```

---

## 📖 Swagger

A documentação interativa pode ser acessada em:

```
http://127.0.0.1:5000/apidocs/
```

---

# 🤝 Contribuição

Contribuições são sempre bem-vindas!

1. Faça um **Fork** do projeto.
2. Crie uma branch para sua funcionalidade.

```bash
git checkout -b feature/NovaFuncionalidade
```

3. Faça o commit.

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

4. Envie para o GitHub.

```bash
git push origin feature/NovaFuncionalidade
```

5. Abra um **Pull Request**.

---

<div align="center">

### ⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!

Desenvolvido utilizando **Flask**, **SQLAlchemy**, **Pydantic** e **Swagger/OpenAPI**.

</div>
