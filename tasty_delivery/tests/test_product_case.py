# tests/test_product_case.py

import unittest
from unittest.mock import MagicMock, patch
from core.application.use_cases.product.product_case import ProductCase
from adapter.repositories.product_repository import ProductRepository
from core.domain.exceptions.exception import ObjectNotFound, DuplicateObject
from core.domain.entities.product import ProductIN, ProductOUT,ProductUpdateIN
from adapter.database.models.product import Product as ProductDB 
from uuid import uuid4
from sqlalchemy.exc import IntegrityError

class TestProductCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock(spec=ProductRepository)
        self.product_case = ProductCase(db=None)
        self.product_case.repository = self.mock_repo

    def test_get_all(self):
        self.mock_repo.get_all.return_value = ["Product1", "Product2"]
        result = self.product_case.get_all()
        self.assertEqual(result, ["Product1", "Product2"])
        self.mock_repo.get_all.assert_called_once()

    def test_get_by_id_found(self):
        self.mock_repo.get_by_id.return_value = "Product1"
        result = self.product_case.get_by_id(1)
        self.assertEqual(result, "Product1")
        self.mock_repo.get_by_id.assert_called_once_with(1)

    def test_get_by_id_not_found(self):
        self.mock_repo.get_by_id.return_value = None
        with self.assertRaises(ObjectNotFound):
            self.product_case.get_by_id(1)
        self.mock_repo.get_by_id.assert_called_once_with(1)

    def test_get_by_category(self):
        self.mock_repo.get_by_category.return_value = ["Product1", "Product2"]
        result = self.product_case.get_by_category(1)
        self.assertEqual(result, ["Product1", "Product2"])
        self.mock_repo.get_by_category.assert_called_once_with(1)

    # @patch('core.application.use_cases.product.product_case.uuid4', return_value='mock-uuid')
    # def test_create_success(self, mock_uuid):
    #     product_in = MagicMock(spec=ProductIN)
    #     product_in.model_dump.return_value = {"name": "Product1"}
    #     product_out = MagicMock(spec=ProductOUT)
    #     self.mock_repo.create.return_value = product_out

    #     result = self.product_case.create(product_in)
    #     self.assertEqual(result, product_out)
    #     self.mock_repo.create.assert_called_once_with(ProductDB(name="Product1", id='mock-uuid'))

    # @patch('core.application.use_cases.product.product_case.uuid4', return_value='mock-uuid')
    # def test_create_duplicate(self, mock_uuid):
    #     product_in = MagicMock(spec=ProductIN)
    #     product_in.model_dump.return_value = {"name": "Product1"}
    #     self.mock_repo.create.side_effect = IntegrityError

    #     with self.assertRaises(DuplicateObject):
    #         self.product_case.create(product_in)
    #     self.mock_repo.create.assert_called_once_with(ProductDB(name="Product1", id='mock-uuid'))

    def test_update(self):
        product_update_in = MagicMock(spec=ProductUpdateIN)
        product_update_in.model_dump.return_value = {"name": "UpdatedProduct"}
        product_out = MagicMock(spec=ProductOUT)
        self.mock_repo.update.return_value = product_out

        result = self.product_case.update(1, product_update_in)
        self.assertEqual(result, product_out)
        self.mock_repo.update.assert_called_once_with(1, {"name": "UpdatedProduct"})

    def test_delete(self):
        self.mock_repo.delete.return_value = "Deleted"
        result = self.product_case.delete(1, "user")
        self.assertEqual(result, "Deleted")
        self.mock_repo.delete.assert_called_once_with(1, "user")

if __name__ == '__main__':
    unittest.main()