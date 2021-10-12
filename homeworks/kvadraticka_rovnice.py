from math import sqrt


def kvadra(a, b, c):
    d = b * b - 4 * a * c
    x1 = 0
    x2 = 0
    if d == 0:
        x = -b / 2 * a
        return x
    elif d > 0:
        x1 = (-b + sqrt(d)) / 2 * a
        x2 = (-b - sqrt(d)) / 2 * a
        return x1, x2
    elif d < 0:
        return "do komplexnich cisel se mi ted kurva rozhodne nechce"

