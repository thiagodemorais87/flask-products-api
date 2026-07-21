from flask import jsonify
from pydantic import ValidationError

def register_error_handlers(app):

    # Captura erros de validação do Pydantic (Retorna HTTP 422)
    @app.errorhandler(ValidationError)
    def handle_pydantic_validation_error(e):
        return jsonify({
            "error": "Erro de validação nos dados enviados",
            "details": e.errors(),
            "status": 422
        }), 422

    # Captura ValueError disparado pelo Service (Ex: Produto não encontrado - HTTP 404)
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({
            "error": str(e),
            "status": 404
        }), 404

    # Captura qualquer erro não previsto no servidor (HTTP 500)
    @app.errorhandler(Exception)
    def handle_generic_error(e):
        return jsonify({
            "error": "Erro interno no servidor",
            "status": 500
        }), 500