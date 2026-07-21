<div align="center">

# 📦 API RESTful de Gerenciamento de Produtos

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-e91e63?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Swagger](https://img.shields.io/badge/Swagger-Doc-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

*API RESTful desenvolvida em Python para gerenciamento completo de catálogo de produtos, construída com arquitetura em camadas e documentação OpenAPI/Swagger integrados.*

[Visão Geral](#-visão-geral) •
[Arquitetura](#-arquitetura-do-projeto) •
[Endpoints](#-endpoints-da-api) •
[Como Executar](#-como-executar) •
[Tratamento de Erros](#-tratamento-de-erros)

</div>

---

## 📌 Visão Geral

Esta aplicação oferece uma solução robusta para o gerenciamento de produtos. O projeto foi projetado seguindo princípios de **Clean Code** e **Arquitetura em Camadas**, garantindo alta manutenibilidade, separação clara de responsabilidades e tratamento centralizado de exceções.

### Key Features
- **CRUD Completo:** Listagem, criação, busca individual, atualização e exclusão de produtos.
- **Validação de Dados:** Schemas estritos controlados via **Pydantic** para prevenção de dados inválidos.
- **Camada de Dados (ORM):** Abstração do banco através do **SQLAlchemy** e padrão **Repository**.
- **Documentação Interativa:** Interface Swagger UI embutida e acessível direto pelo navegador.
- **Manipulação Global de Erros:** Handlers centrais para captura de exceções `HTTP 404`, `422` e `500`.

---

## 🏗 Arquitetura do Projeto

A aplicação segue a separação de responsabilidades em 5 camadas principais:

```text
  Client (Swagger / Front-end / Postman)
                   │
                   ▼
       ┌──────────────────────┐
       │   Routes / Blueprints│ ── HTTP Requests & JSON Responses
       └───────────┬──────────┘
                   │
                   ▼
       ┌──────────────────────┐
       │   Services Layer     │ ── Business Rules & Orchestration
       └─────┬────────────┬───┘
             │            │
             ▼            ▼
┌──────────────────┐  ┌──────────────────┐
│ Pydantic Schemas │  │ Repositories     │ ── Data Validation & DB Queries
└──────────────────┘  └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │ Database (Model) │
                      └──────────────────┘

## Estrutura de Diretórios
```text

flask-products-api/
├── app/
│   ├── models/          # Entidades do Banco de Dados (SQLAlchemy)
│   ├── repositories/    # Consultas diretas ao Banco de Dados
│   ├── routes/          # Endpoints HTTP / Blueprints e Swagger Docs
│   ├── schemas/         # Validação de dados e entrada (Pydantic)
│   ├── services/        # Regras de negócio da aplicação
│   ├── errors.py        # Captura e tratamento global de exceções
│   ├── extensions.py    # Inicialização das extensões (db, etc)
│   └── __init__.py      # Factory da aplicação Flask
├── instance/            # Arquivos locais (ex: banco SQLite)
├── .gitignore
├── README.md
├── requirements.txt     # Dependências do projeto
└── run.py               # Ponto de entrada para inicialização do servidor


Método,Endpoint,Descrição,Status HTTP
GET,/api/products,Lista todos os produtos cadastrados,200 OK
POST,/api/products,Cadastra um novo produto,201 Created
GET,/api/products/<id>,Busca um produto pelo ID,200 OK / 404 Not Found
PUT,/api/products/<id>,Atualiza os dados de um produto,200 OK / 404 Not Found
DELETE,/api/products/<id>,Remove um produto do banco,200 OK / 404 Not Found
