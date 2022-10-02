import unittest
from jsonvalidator import validate_json


class TestValidateJson(unittest.TestCase):
    def test_valid_json(self):
        schema = {
            "name": ["required", "string"],
            "phone": ["required", "string"],
            "email": ["required", "string"],
            "test": ["required", "boolean"],
            "job": {
                "title": ["required", "string"],
                "department": ["required", "string"],
                "salary": [
                    {
                        "gross": ["required", "float"],
                        "net": ["required", "float"],
                    },
                ],
            },
            "pet_names": ["required", "list"],
        }

        json_object = {
            "name": "John Doe",
            "phone": "+1 5555 5555",
            "email": "email",
            "test": True,
            "job": {
                "title": "Software Engineer",
                "department": "Engineering",
                "salary": [
                    {
                        "gross": 50000.00,
                        "net": 50000.00,
                    },
                ],
            },
            "pet_names": ["my pet"],
        }

        res = validate_json(schema=schema, json_object=json_object)
        self.assertEqual(res["valid"], True, "Should be valid")

    def test_invalid_json_missing_schema_key(self):
        schema = {
            "name": ["required", "string"],
            "phone": ["required", "string"],
            "email": ["required", "string"],
            "job": {
                "title": ["required", "string"],
                "department": ["required", "string"],
                "salary": [
                    {
                        "gross": ["required", "float"],
                        "net": ["required", "float"],
                    },
                ],
            },
            "pet_names": ["required", "list"],
        }

        json_object = {
            "name": "John Doe",
            "phone": "+1 5555 5555",
            "email": "email",
            "test": True,
            "job": {
                "title": "Software Engineer",
                "department": "Engineering",
                "salary": [
                    {
                        "gross": 50000.00,
                        "net": 50000.00,
                    },
                ],
            },
            "pet_names": ["my pet"],
        }

        res = validate_json(schema=schema, json_object=json_object)
        self.assertEqual(res["valid"], False, "Should be invalid")

    def test_invalid_json_missing_json_key(self):
        schema = {
            "name": ["required", "string"],
            "phone": ["required", "string"],
            "email": ["required", "string"],
            "test": ["required", "boolean"],
            "job": {
                "title": ["required", "string"],
                "department": ["required", "string"],
                "salary": [
                    {
                        "gross": ["required", "float"],
                        "net": ["required", "float"],
                    },
                ],
            },
            "pet_names": ["required", "list"],
        }

        json_object = {
            "name": "John Doe",
            "phone": "+1 5555 5555",
            "test": True,
            "job": {
                "title": "Software Engineer",
                "department": "Engineering",
                "salary": [
                    {
                        "gross": 50000.00,
                        "net": 50000.00,
                    },
                ],
            },
            "pet_names": ["my pet"],
        }

        res = validate_json(schema=schema, json_object=json_object)
        self.assertEqual(res["valid"], False, "Should be invalid")

    def test_invalid_json_missing_schema_object(self):
        schema = {
            "name": ["required", "string"],
            "phone": ["required", "string"],
            "email": ["required", "string"],
            "test": "",
            "job": {
                "title": ["required", "string"],
                "department": ["required", "string"],
                "salary": [
                    {
                        "gross": ["required", "float"],
                        "net": ["required", "float"],
                    },
                ],
            },
            "pet_names": ["required", "list"],
        }

        json_object = {
            "name": "John Doe",
            "phone": "+1 5555 5555",
            "email": "email",
            "test": True,
            "job": {
                "title": "Software Engineer",
                "department": "Engineering",
                "salary": [
                    {
                        "gross": 50000.00,
                        "net": 50000.00,
                    },
                ],
            },
            "pet_names": ["my pet"],
        }

        res = validate_json(schema=schema, json_object=json_object)
        self.assertEqual(res["valid"], False, "Should be invalid")

    def test_invalid_json_missing_required_key(self):
        schema = {
            "name": ["required", "string"],
            "phone": ["required", "string"],
            "email": ["required", "string"],
            "test": ["required", "string"],
            "job": {
                "title": ["required", "string"],
                "department": ["required", "string"],
                "salary": [
                    {
                        "gross": ["required", "float"],
                        "net": ["required", "float"],
                    },
                ],
            },
            "pet_names": ["required", "list"],
        }

        json_object = {
            "name": "John Doe",
            "phone": "+1 5555 5555",
            "email": "",
            "test": True,
            "job": {
                "title": "Software Engineer",
                "department": "Engineering",
                "salary": [
                    {
                        "gross": 50000.00,
                        "net": 50000.00,
                    },
                ],
            },
            "pet_names": ["my pet"],
        }

        res = validate_json(schema=schema, json_object=json_object)
        self.assertEqual(res["valid"], False, "Should be invalid")


if __name__ == "__main__":
    unittest.main()
