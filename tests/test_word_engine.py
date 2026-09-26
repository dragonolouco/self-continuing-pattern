import unittest

from src.word_engine import default_game_knowledge


class WordEngineTests(unittest.TestCase):
    def setUp(self):
        self.knowledge = default_game_knowledge()

    def test_word_has_structured_meaning(self):
        jogo = self.knowledge.get("jogo")
        self.assertEqual(jogo.category, "atividade")
        self.assertIn("mecânicas", jogo.relations["possui"])

    def test_can_follow_a_subchain(self):
        chain = self.knowledge.chain("jogo", "pode_ter")
        self.assertIn("pode_ter->terror", chain)
        self.assertIn("pode_ter->aventura", chain)

    def test_composes_phrase_context(self):
        result = self.knowledge.compose_game_phrase(
            "jogo de terror com exploração"
        )
        self.assertEqual(result["entidade"], "jogo")
        self.assertEqual(result["gênero"], "terror")
        self.assertEqual(result["mecânica"], "exploração")

    def test_unknown_concept_is_not_invented(self):
        with self.assertRaises(KeyError):
            self.knowledge.compose_game_phrase("jogo de ficção")


if __name__ == "__main__":
    unittest.main()
