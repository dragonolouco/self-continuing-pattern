"""Motor didático de aritmética por regras fundamentais.

As operações percorrem os dígitos e mantêm estado explícito. O objetivo é
mostrar a estrutura, não substituir bibliotecas de inteiros de produção.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Step:
    position: int
    left: int
    right: int
    state_in: int
    written: int
    state_out: int


def _digits(value: int) -> list[int]:
    if value < 0:
        raise ValueError("esta versão aceita apenas inteiros não negativos")
    return [int(char) for char in str(value)][::-1]


def add_with_trace(left: int, right: int) -> tuple[int, list[Step]]:
    """Soma dois inteiros por colunas e retorna resultado e estados."""
    a, b = _digits(left), _digits(right)
    steps: list[Step] = []
    carry = 0
    output: list[int] = []

    for position in range(max(len(a), len(b))):
        da = a[position] if position < len(a) else 0
        db = b[position] if position < len(b) else 0
        total = da + db + carry
        written, next_carry = total % 10, total // 10
        steps.append(Step(position, da, db, carry, written, next_carry))
        output.append(written)
        carry = next_carry

    if carry:
        output.append(carry)

    result = int("".join(map(str, output[::-1]))) if output else 0
    if result != left + right:
        raise AssertionError("invariante de soma violada")
    return result, steps


def subtract_with_trace(left: int, right: int) -> tuple[int, list[Step]]:
    """Subtrai por colunas; exige left >= right e usa empréstimo explícito."""
    if left < right:
        raise ValueError("esta versão exige left >= right")
    a, b = _digits(left), _digits(right)
    steps: list[Step] = []
    borrow = 0
    output: list[int] = []

    for position in range(len(a)):
        da = a[position]
        db = b[position] if position < len(b) else 0
        available = da - borrow
        next_borrow = 1 if available < db else 0
        written = available + (10 if next_borrow else 0) - db
        steps.append(Step(position, da, db, borrow, written, next_borrow))
        output.append(written)
        borrow = next_borrow

    if borrow:
        raise AssertionError("empréstimo não resolvido")
    result = int("".join(map(str, output[::-1]))) if output else 0
    if result != left - right:
        raise AssertionError("invariante de subtração violada")
    return result, steps


def format_trace(steps: list[Step]) -> str:
    """Formata estados para inspeção humana."""
    return "\n".join(
        f"coluna {s.position}: {s.left} + {s.right} + estado {s.state_in} "
        f"-> escreve {s.written}, novo estado {s.state_out}"
        for s in steps
    )


if __name__ == "__main__":
    result, trace = add_with_trace(5897, 7648)
    print(f"5897 + 7648 = {result}")
    print(format_trace(trace))
