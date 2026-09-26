import unittest

from src.text_engine import Entity, find_without_character


class TextEngineTests(unittest.TestCase):
    def setUp(self):
        self.entities = [
            Entity("Brasil", "país"),
            Entity("Chile", "país"),
            Entity("Peru", "país"),
            Entity("Canadá", "país"),
            Entity("Recife", "cidade", "Brasil"),
        ]

    def test_finds_countries_without_letter(self):
        result = find_without_character(
            self.entities, category="país", character="a"
        )
        self.assertEqual([entity.name for entity in result], ["Chile", "Peru"])

    def test_accent_is_structurally_normalized(self):
        result = find_without_character(
            self.entities, category="país", character="a"
        )
        self.assertNotIn("Canadá", [entity.name for entity in result])

    def test_category_is_part_of_the_rule(self):
        result = find_without_character(
            self.entities, category="cidade", character="a"
        )
        self.assertEqual([entity.name for entity in result], ["Recife"])

    def test_rejects_more_than_one_character(self):
        with self.assertRaises(ValueError):
            find_without_character(self.entities, category="país", character="ab")


if __name__ == "__main__":
    unittest.main()
