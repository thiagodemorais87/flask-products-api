<div align="center">

# 📦 API RESTful de Gerenciamento de Produtos

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

*API RESTful robusta desenvolvida em Python para gerenciamento de catálogo de produtos, integrada ao banco de dados PostgreSQL executado em containers Docker e documentada com Swagger/OpenAPI.*

</div>

---

# 📌 Principais Recursos

- ✅ **Persistência em Tempo Real:** Banco de dados PostgreSQL executando em container Docker com armazenamento persistente via volumes.
- ✅ **CRUD Completo:** Endpoints para criação, consulta, atualização e remoção de produtos.
- ✅ **Integração Facilitada:** API preparada para consumo por aplicações Web, Mobile e Front-end.
- ✅ **Validação de Dados:** Utilização do Pydantic para garantir integridade dos dados recebidos.
- ✅ **Arquitetura em Camadas:** Organização em Routes, Services, Repositories, Schemas e Models.
- ✅ **Documentação Interativa:** Swagger/OpenAPI disponível diretamente no navegador.

---

# 🏗 Arquitetura

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
               PostgreSQL
                (Docker)
```

---

# 📁 Estrutura do Projeto

```text
flask-products-api/
│
├── app/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── errors.py
│   ├── extensions.py
│   └── __init__.py
│
├── instance/
├── docker-compose.yml
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

# 🛣 Endpoints da API

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/api/products` | Lista todos os produtos |
| POST | `/api/products` | Cria um novo produto |
| GET | `/api/products/<id>` | Busca produto pelo ID |
| PUT | `/api/products/<id>` | Atualiza um produto |
| DELETE | `/api/products/<id>` | Remove um produto |

---

# 📦 Exemplo de Requisição

## POST `/api/products`

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

# 🚀 Como Executar o Projeto

## Pré-requisitos

- Python 3.10+
- Docker
- Docker Desktop

---

## 1. Clone o repositório

```bash
git clone https://github.com/thiagodemorais87/flask-products-api.git

cd flask-products-api
```

---

## 2. Crie e ative o ambiente virtual

### Windows (PowerShell)

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

## 4. Inicie o PostgreSQL com Docker Compose

```bash
docker compose up -d
```

Verifique se o container está em execução:

```bash
docker compose ps
```

---

## 5. Execute a API Flask

```bash
python run.py
```

A aplicação estará disponível em:

```
http://127.0.0.1:5000
```

---

# 📖 Documentação Swagger

A documentação interativa pode ser acessada em:

```
http://127.0.0.1:5000/apidocs/
```

---

# 🛠️ Comandos Úteis do Docker

### Verificar containers

```bash
docker compose ps
```

### Visualizar logs do PostgreSQL

```bash
docker compose logs -f db
```

### Parar os containers

```bash
docker compose down
```

### Reiniciar os containers

```bash
docker compose restart
```

### Remover containers e volumes

```bash
docker compose down -v
```

---

# 🚨 Tratamento de Erros

A API retorna respostas padronizadas para erros de validação e recursos inexistentes.

Exemplo de erro de validação:

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

# 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um **Fork** do projeto.

2. Crie uma branch:

```bash
git checkout -b feature/NovaFuncionalidade
```

3. Faça seus commits:

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

4. Envie para o GitHub:

```bash
git push origin feature/NovaFuncionalidade
```

5. Abra um **Pull Request**.

---

<div align="center">

### ⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!

**Flask • PostgreSQL • SQLAlchemy • Docker • Swagger/OpenAPI**

</div>
