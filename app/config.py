import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta_aqui")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False