from typing import List

from sqlalchemy.exc import IntegrityError

from adapter.database.models.product import Product as ProductDb
from core.domain.repositories.iproduct_repository import IProductRepository


class ProductRepository(IProductRepository):

    def __init__(self, db=None):
        self.db = db

    def get_all(self) -> List[ProductDb]:
        result = self.db.query(ProductDb).all()
        return result
