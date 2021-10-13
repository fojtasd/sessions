from typing import Optional
from dataclasses import dataclass


# toto je alias struktury z C/C++ - tzv. dataklása
@dataclass
class Pair:
    a: Optional[float]
    b: Optional[float]


# a takto se používá:
# muj_pair = Pair(10.0, 20.0)
# print(muj_pair.a)
# print(muj_pair.b)


# když chci zkontrolovat Optional, jestli má hodnotu nebo ne, tak použiju:
# if muj_optional_prom is not None:
#     ...
# normálně kontrola proměnných dělám s rovnítkem:
# if hodnota == 10:
#     ...
# ale u zjisťování jestli je proměnná null (None) musím použít klíčové slovo is

# trojclenka_prima -> code style pro pythonní funkce je snake_case
def trojclenka_prima(first: Pair, second: Pair) -> float:
    kontrola_hodnot = 0
    missing_first = False
    missing_second = False
    if first.a is None:
        # hint: kontrola_hodnot += 1
        kontrola_hodnot = kontrola_hodnot + 1
        missing_first = True
    if first.b is None:
        kontrola_hodnot = kontrola_hodnot + 1
        missing_first = True
    if second.a is None:
        kontrola_hodnot = kontrola_hodnot + 1
        missing_second = True
    if second.b is None:
        kontrola_hodnot = kontrola_hodnot + 1
        missing_second = True
    if kontrola_hodnot != 1:
        raise RuntimeError("Chyba")
    if missing_first:
        if first.a is None:
            first.a = first.b * second.a / second.b
            return first, second
        if first.b is None:
            first.b = first.a * second.b / second.a
            return first, second
    if missing_second:
        if second.a is None:
            second.a = first.a * second.b / first.b
            return first, second
        if second.b is None:
            second.b = first.b * second.a / first.a
            return first, second


print(trojclenka_prima(Pair(None, 50), Pair(9, 450)))
print(trojclenka_prima(Pair(1, None), Pair(9, 450)))
print(trojclenka_prima(Pair(1, 50), Pair(None, 450)))
print(trojclenka_prima(Pair(1, 50), Pair(9, None)))
# inspirace https://www.vypocitejto.cz/trojclenka/

# python nemá ||, &&
# místo nich má or, and

# python bool hodnoty jsou True a False (velké T a F)

# 1: from (a) -> to (b): poměr je koeficient = to / from
# 2: from (a) -> to (b): poměr počítám podle toho kde mi chybí
# -----------
# 1: 100 -> ?
# 2: 50 -> 500: koef = 500 / 50
# -----------
# 1: ? -> 100
# 2: 50 -> 500: koef = 500 / 50
