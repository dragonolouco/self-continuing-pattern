"""Consultas textuais determinísticas sobre entidades categorizadas."""

from dataclasses import dataclass
import unicodedata


@dataclass(frozen=True)
class Entity:
    name: str
    category: str
    country: str | None = None


def normalize_text(value: str) -> str:
    """Normaliza caixa e acentos para comparações estruturais."""
    decomposed = unicodedata.normalize("NFD", value.casefold())
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")


def find_without_character(
    entities: list[Entity],
    *,
    category: str,
    character: str,
    country: str | None = None,
) -> list[Entity]:
    """Retorna entidades que não contêm o caractere procurado.

    O resultado depende explicitamente da base fornecida e dos filtros.
    A função não inventa fatos sobre entidades ausentes da base.
    """
    target = normalize_text(character)
    if len(target) != 1:
        raise ValueError("character deve ser um único caractere")

    return [
        entity
        for entity in entities
        if entity.category == category
        and (country is None or entity.country == country)
        and target not in normalize_text(entity.name)
    ]


if __name__ == "__main__":
    countries = [
        Entity("Brasil", "país"),
        Entity("Chile", "país"),
        Entity("Peru", "país"),
        Entity("Canadá", "país"),
    ]
    result = find_without_character(countries, category="país", character="a")
    print([entity.name for entity in result])
