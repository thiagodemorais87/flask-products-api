from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/products', methods=['GET'])
def get_products():
    """
    Listar todos os produtos
    ---
    responses:
      200:
        description: Lista de produtos retornada com sucesso
    """
    products = ProductService.list_products()
    return jsonify({
        "data": products,
        "message": "Sucesso",
        "status": 200
    }), 200


@product_bp.route('/api/products', methods=['POST'])
def create_product():
    """
    Cadastrar um novo produto
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - price
            - stock
          properties:
            name:
              type: string
              example: "Teclado Mecânico"
            price:
              type: number
              example: 250.0
            stock:
              type: integer
              example: 10
    responses:
      201:
        description: Produto criado com sucesso
      422:
        description: Erro de validação de dados
    """
    data = request.get_json()
    new_product = ProductService.create_product(data)
    
    return jsonify({
        "data": new_product,
        "message": "Produto criado com sucesso",
        "status": 201
    }), 201


@product_bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Buscar produto por ID
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto encontrado
      404:
        description: Produto não encontrado
    """
    try:
        product = ProductService.get_product(product_id)
        return jsonify({
            "data": product,
            "message": "Sucesso",
            "status": 200
        }), 200
    except ValueError as e:
        return jsonify({
            "error": str(e),
            "status": 404
        }), 404


@product_bp.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Atualizar um produto existente
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto a ser atualizado
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Teclado RGB"
            price:
              type: number
              example: 280.0
            stock:
              type: integer
              example: 15
    responses:
      200:
        description: Produto atualizado com sucesso
      404:
        description: Produto não encontrado
    """
    try:
        data = request.get_json()
        updated_product = ProductService.update_product(product_id, data)
        return jsonify({
            "data": updated_product,
            "message": "Produto atualizado com sucesso",
            "status": 200
        }), 200
    except ValueError as e:
        return jsonify({
            "error": str(e),
            "status": 404
        }), 404


@product_bp.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Remover um produto por ID
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto a ser removido
    responses:
      200:
        description: Produto deletado com sucesso
      404:
        description: Produto não encontrado
    """
    try:
        ProductService.delete_product(product_id)
        return jsonify({
            "message": "Produto deletado com sucesso",
            "status": 200
        }), 200
    except ValueError as e:
        return jsonify({
            "error": str(e),
            "status": 404
        }), 404