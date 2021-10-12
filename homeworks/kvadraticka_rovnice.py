from math import sqrt


def kvadra(a, b, c):
    d = b * b - 4 * a * c
    print((-b + sqrt(d)))
    if d == 0:
        x = float(-b / (2 * a))
        return x
    elif d > 0:
        x1 = float((-b + sqrt(d)) / (2 * a))
        x2 = float((-b - sqrt(d)) / (2 * a))
        return x1, x2
    elif d < 0:
        return "do komplexnich cisel se mi ted kurva rozhodne nechce"


print(kvadra(2, -11, 14))
print("3.5, 2")
print("----------")

print(kvadra(1, 2, -63))
print("7, -9")
print("----------")


print(kvadra(2, 9, 0))
print("0, -4.5")
print("----------")