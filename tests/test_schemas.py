import json
import unittest
from pathlib import Path


class SchemaTests(unittest.TestCase):
    def test_all_schemas_are_valid_json_schema_documents(self):
        schema_dir = Path(__file__).parents[1] / "schemas"
        for path in sorted(schema_dir.glob("*.schema.json")):
            with self.subTest(schema=path.name):
                schema = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertEqual(schema["type"], "object")
                self.assertTrue(schema["required"])
                for field in schema["required"]:
                    self.assertIn(field, schema["properties"])


if __name__ == "__main__":
    unittest.main()
