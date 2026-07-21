from flask import jsonify

def api_response(data=None, message="Sucesso", status_code=200):
    return jsonify({
        "status": status_code,
        "message": message,
        "data": data
    }), status_code

def api_error(message="Erro na requisição", status_code=400, errors=None):
    return jsonify({
        "status": status_code,
        "error": message,
        "details": errors
    }), status_code