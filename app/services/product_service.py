from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductCreateSchema, ProductUpdateSchema

class ProductService:
    @staticmethod
    def list_products():
        products = ProductRepository.get_all()
        return [p.to_dict() for p in products]

    @staticmethod
    def create_product(data: dict):
        # Valida os dados de entrada com Pydantic
        validated_data = ProductCreateSchema(**data)
        
        # Executa a regra de criação
        product = ProductRepository.create(
            name=validated_data.name,
            price=validated_data.price,
            stock=validated_data.stock
        )
        return product.to_dict()

    @staticmethod
    def get_product(product_id: int):
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Produto não encontrado.")
        return product.to_dict()

    @staticmethod
    def update_product(product_id: int, data: dict):
        # Verifica se o produto existe
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Produto não encontrado.")
        
        # Valida os dados de atualização (campos opcionais)
        validated_data = ProductUpdateSchema(**data)
        
        # Executa a atualização no banco
        updated_product = ProductRepository.update(
            product=product,
            name=validated_data.name,
            price=validated_data.price,
            stock=validated_data.stock
        )
        return updated_product.to_dict()

    @staticmethod
    def delete_product(product_id: int):
        # Verifica se o produto existe
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Produto não encontrado.")
        
        # Remove do banco de dados
        ProductRepository.delete(product)
        return True