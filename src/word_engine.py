"""Protótipo explícito da camada de palavras e significados."""

from dataclasses import dataclass, field


@dataclass
class Concept:
    term: str
    definition: str
    category: str
    relations: dict[str, list[str]] = field(default_factory=dict)


class WordKnowledge:
    def __init__(self, concepts: list[Concept] | None = None):
        self.concepts = {concept.term: concept for concept in concepts or []}

    def add(self, concept: Concept) -> None:
        self.concepts[concept.term] = concept

    def get(self, term: str) -> Concept:
        try:
            return self.concepts[term.casefold()]
        except KeyError as exc:
            raise KeyError(f"conceito desconhecido: {term}") from exc

    def chain(self, term: str, relation: str | None = None) -> list[str]:
        """Percorre uma cadeia de relações com ordem determinística."""
        concept = self.get(term)
        if relation is None:
            result = []
            for relation_name, targets in concept.relations.items():
                result.extend(f"{relation_name}->{target}" for target in targets)
            return result
        return [f"{relation}->{target}" for target in concept.relations.get(relation, [])]

    def compose_game_phrase(self, phrase: str) -> dict[str, object]:
        """Compõe uma forma simples: 'jogo de X com Y'."""
        tokens = phrase.casefold().split()
        if not tokens or tokens[0] != "jogo":
            raise ValueError("a forma esperada começa com 'jogo'")

        result: dict[str, object] = {"entidade": "jogo", "tokens": tokens}
        if "de" in tokens:
            start = tokens.index("de") + 1
            end = tokens.index("com") if "com" in tokens[start:] else len(tokens)
            genre = " ".join(tokens[start:end])
            self.get(genre)
            result["gênero"] = genre
        if "com" in tokens:
            start = tokens.index("com") + 1
            mechanic = " ".join(tokens[start:])
            self.get(mechanic)
            result["mecânica"] = mechanic
        return result


def default_game_knowledge() -> WordKnowledge:
    knowledge = WordKnowledge(
        [
            Concept(
                "jogo",
                "atividade estruturada com regras e objetivo",
                "atividade",
                {
                    "possui": ["regras", "objetivo", "mecânicas"],
                    "pode_ter": ["terror", "aventura", "estratégia"],
                },
            ),
            Concept("terror", "gênero que produz medo ou tensão", "gênero"),
            Concept("aventura", "gênero centrado em exploração e desafios", "gênero"),
            Concept("estratégia", "gênero centrado em decisões e planejamento", "gênero"),
            Concept("exploração", "mecânica de descobrir espaços ou informações", "mecânica"),
            Concept("regras", "restrições que definem ações válidas", "estrutura"),
            Concept("objetivo", "resultado que orienta a atividade", "estrutura"),
            Concept("mecânicas", "formas de interação disponíveis no sistema", "estrutura"),
        ]
    )
    return knowledge


if __name__ == "__main__":
    knowledge = default_game_knowledge()
    print(knowledge.chain("jogo", "possui"))
    print(knowledge.compose_game_phrase("jogo de terror com exploração"))
