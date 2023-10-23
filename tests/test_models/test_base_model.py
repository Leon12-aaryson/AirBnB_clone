#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing of the BaseModel class."""

    def test_id_assigned(self):
        model = BaseModel()
        self.assertTrue(model.id)

    def test_id_is_string(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_assign(self):
        m = BaseModel()
        self.assertTrue(m.created_at)

    def test_updated_at_assign(self):
        m = BaseModel()
        self.assertTrue(m.created_at)

    def assert_updated_at_equal_created_at(self):
        m = BaseModel()
        self.assertEqual(m.created_at, m.updated_at)

    def test_updated_at_changes(self):
        m = BaseModel()
        # store current updated at
        c_updated_at = m.updated_at
        m.save()
        self.assertNotEqual(m.updated_at, c_updated_at)

    def test_save(self):
        m = BaseModel()
        # store current updated at
        c_updated_at = m.updated_at
        m.save()
        self.assertNotEqual(m.updated_at, c_updated_at)

    def test_to_dict(self):
        m = BaseModel()
        m_dict = m.to_dict()
        self.assertEqual(m_dict['__class__'], m.__class__.__name__)
        self.assertEqual(m_dict['created_at'], m.created_at.isoformat())
        self.assertEqual(m_dict['updated_at'], m.updated_at.isoformat())

    def test_str(self):
        m = BaseModel()
        test_data = f"[{m.__class__.__name__}] ({m.id}) {m.__dict__}"
        self.assertEqual(m.__str__(), test_data)


class TestBaseModel_from_dict(unittest.TestCase):
    def test_no_arguments_passed(self):
        b = BaseModel()
        self.assertTrue(b.id)

    def test_arguments_passed(self):
        test_data = {'id': 'a592f7d4-ba37-44b8-a381-4b9f51639895',
                     'created_at': '2023-10-17T07:29:05.227683',
                     'updated_at': '2023-10-17T07:29:05.227683',
                     'name': 'My_First_Model', 'my_number': 89,
                     '__class__': 'BaseModel'}

        b = BaseModel(**test_data)
        self.assertEqual(b.id, test_data["id"])

        created_at = datetime.strptime(test_data['created_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(b.created_at, created_at)

        updated_at = datetime.strptime(test_data['updated_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(b.updated_at, updated_at)

        self.assertEqual(b.name, "My_First_Model")
        self.assertEqual(str(b.my_number), "89")


if __name__ == "__main__":
    unittest.main()
