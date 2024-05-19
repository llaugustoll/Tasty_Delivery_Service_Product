# tests/test_category_case.py

import unittest
from unittest.mock import MagicMock, patch
from uuid import uuid4
from sqlalchemy.exc import IntegrityError
from adapter.database.models.category import Category as CategoryDB
from adapter.repositories.category_repository import CategoryRepository
from core.application.use_cases.category.category_case import CategoryCase
from core.domain.entities.category import CategoryOUT, CategoryIN
from core.domain.exceptions.exception import DuplicateObject, ObjectNotFound

class TestCategoryCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock(spec=CategoryRepository)
        self.category_case = CategoryCase(db=None)
        self.category_case.repository = self.mock_repo

    def test_get_all(self):
        self.mock_repo.get_all.return_value = ["Category1", "Category2"]
        result = self.category_case.get_all()
        self.assertEqual(result, ["Category1", "Category2"])
        self.mock_repo.get_all.assert_called_once()

    def test_get_by_id_found(self):
        self.mock_repo.get_by_id.return_value = "Category1"
        result = self.category_case.get_by_id(1)
        self.assertEqual(result, "Category1")
        self.mock_repo.get_by_id.assert_called_once_with(1)

    def test_get_by_id_not_found(self):
        self.mock_repo.get_by_id.return_value = None
        with self.assertRaises(ObjectNotFound):
            self.category_case.get_by_id(1)
        self.mock_repo.get_by_id.assert_called_once_with(1)

    @patch('core.application.use_cases.category.category_case.uuid4', return_value='mock-uuid')
    def test_create_success(self, mock_uuid):
        category_out = MagicMock(spec=CategoryOUT)
        category_out.model_dump.return_value = {"name": "Category1"}
        category_db = MagicMock(spec=CategoryDB)
        self.mock_repo.create.return_value = category_db

        result = self.category_case.create(category_out)
        self.assertEqual(result, category_db)
        self.mock_repo.create.assert_called_once_with(CategoryDB(name="Category1", id='mock-uuid'))

    @patch('core.application.use_cases.category.category_case.uuid4', return_value='mock-uuid')
    def test_create_duplicate(self, mock_uuid):
        category_out = MagicMock(spec=CategoryOUT)
        category_out.model_dump.return_value = {"name": "Category1"}
        self.mock_repo.create.side_effect = IntegrityError

        with self.assertRaises(DuplicateObject):
            self.category_case.create(category_out)
        self.mock_repo.create.assert_called_once_with(CategoryDB(name="Category1", id='mock-uuid'))

    def test_update(self):
        category_in = MagicMock(spec=CategoryIN)
        category_in.model_dump.return_value = {"name": "UpdatedCategory"}
        category_out = MagicMock(spec=CategoryOUT)
        self.mock_repo.update.return_value = category_out

        result = self.category_case.update(1, category_in)
        self.assertEqual(result, category_out)
        self.mock_repo.update.assert_called_once_with(1, {"name": "UpdatedCategory"})

    def test_delete(self):
        self.mock_repo.delete.return_value = "Deleted"
        result = self.category_case.delete(1, "user")
        self.assertEqual(result, "Deleted")
        self.mock_repo.delete.assert_called_once_with(1, "user")

if __name__ == '__main__':
    unittest.main()
