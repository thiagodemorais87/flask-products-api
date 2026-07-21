from flask import Flask
from app.config import Config
from app.extensions import db, swagger
from app.routes.product_routes import product_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    swagger.init_app(app)  # <--- Linha adicionada

    # Registrar Blueprints
    app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()

    return app