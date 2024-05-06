from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from adapter.database.db import get_db
from core.application.use_cases.product.product_case import ProductCase
from core.domain.entities.product import ProductOUT, ProductIN, ProductUpdateIN
from core.domain.exceptions.exception_schema import ObjectNotFound, ObjectDuplicated
# from security.base import get_current_user


class ProductController:

    def __init__(self, product_case: ProductCase = None):
        self.router = APIRouter(tags=["Products"], prefix='/products2')
        self.router.add_api_route(
            path="/",
            endpoint=self.products,
            methods=["GET"],
            response_model=List[ProductOUT],
            status_code=200
        )
        self._product_case = product_case

    async def products(self, db=Depends(get_db)):
        """
        Retorna todos os produtos cadastrados
        """
        return self._product_case(db).get_all()
