from app.extensions import db
from app.models.product_model import ProductModel

class ProductRepository:
    @staticmethod
    def get_all():
        return ProductModel.query.all()

    @staticmethod
    def get_by_id(product_id: int):
        return ProductModel.query.get(product_id)

    @staticmethod
    def create(name: str, price: float, stock: int):
        product = ProductModel(name=name, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product: ProductModel, name: str = None, price: float = None, stock: int = None):
        """Atualiza apenas os campos enviados pelo usuário"""
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock
            
        db.session.commit()
        return product

    @staticmethod
    def delete(product: ProductModel):
        db.session.delete(product)
        db.session.commit()