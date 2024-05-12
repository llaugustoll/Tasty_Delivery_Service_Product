from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from adapter.database.models.category import Category as CategoryDB
from adapter.repositories.category_repository import CategoryRepository
from core.application.use_cases.category.icategory_case import ICategoryCase
from core.domain.entities.category import CategoryOUT
from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound
from logger import logger


class CategoryCase(ICategoryCase):

    def __init__(self, db=None):
        self.repository = CategoryRepository(db)

    def get_all(self):
        result = self.repository.get_all()
        return result

    def get_by_id(self, id):
        result = self.repository.get_by_id(id)
        if not result:
            msg = f"Categoria {id} não encontrado"
            logger.warning(msg)
            raise ObjectNotFound(msg, 404)
        return result

    def create(self, obj: CategoryOUT) -> CategoryOUT:
        # obj.created_by = self.current_user.id
        try:
            id = uuid4()
            return self.repository.create(CategoryDB( 
                **obj.model_dump(exclude_none=True),
                id=id
                )
            )
        except IntegrityError:
            msg = "Categoria já existente na base de dados"
            logger.warning(msg)
            raise DuplicateObject(msg, 409)

    def update(self, id, new_values: CategoryOUT) -> CategoryOUT:
        new_values.id = None
        # new_values.updated_by = self.current_user.id
        return self.repository.update(id, new_values.model_dump(exclude_none=True))

    def delete(self, id):
        return self.repository.delete(id)
