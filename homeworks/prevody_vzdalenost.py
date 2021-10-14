from typing import Optional
from dataclasses import dataclass


# toto je alias struktury z C/C++ - tzv. dataklása
@dataclass
class Hodnota:
    seznam = {
        "pikometr": 0.000000000001,
        "nanometr": 0.000000001,
        "mikrometr": 0.000001,
        "milimetr": 0.001,
        "centimetr": 0.01,
        "decimetr": 0.1,
        "palec": 0.0254,
        "stopa": 0.3048,
        "loket": 0.593,
        "yard": 0.9144,
        "metr": 1,
        "sáh": 1.7928,
        "kilometr": 1000,
        "míle": 1609
    }


def prevod(hodnota: float, stavajici_jednotka: str, pozadovana_jednotka: str):
    koeficient = 0
    koeficient2 = 0
    vysledny_prevod = 0
    koeficient = Hodnota.seznam[stavajici_jednotka]
    koeficient2 = Hodnota.seznam[pozadovana_jednotka]
    vysledny_prevod = float(hodnota) * float(koeficient) / float(koeficient2)
    return vysledny_prevod


print(prevod(50, "kilometr", "centimetr"))
