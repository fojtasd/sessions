from math import sqrt


def kvadra(a, b, c, vysledek1, vysledek2):
    vysledky = (vysledek1, vysledek2)
    d = b * b - 4 * a * c
    if d == 0:
        x1 = float(-b / (2 * a))
        reseni = (x1, "none")
    elif d > 0:
        x1 = float((-b + sqrt(d)) / (2 * a))
        x2 = float((-b - sqrt(d)) / (2 * a))
        reseni = (x1, x2)
    elif d < 0:
        reseni = ("none", "none")
    # kontrolní bod
    if vysledky == reseni:
        print("Korektně vypočteno")
    else:
        print("Někde nastala chyba")


kvadra(2, -11, 14, 3.5, 2)
kvadra(1, 2, -63, 7, -9)
kvadra(2, 9, 0, 0, -4.5)
