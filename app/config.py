import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta_aqui")
    
    # Substituído 'sqlite:///database.db' pela string de conexão do PostgreSQL do Docker
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "postgresql://root:rootpassword@localhost:5439/products_db"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False