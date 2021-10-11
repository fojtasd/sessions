import time
import basics3_calc
from time import time
from basics3_calc import calc

#print("basics:", __name__)
# dunder = double underscore
# __name__ = co to znamená?
# __name__ == "__main__"
# ctrl + click na nazev souboru otevira soubor
# python pomocí importu spouští daný skript/soubor
# levy alt + enter = doporučené akce
# f = funkce (v idečku), c je konstanta
# from BALÝČEK import SYMBOL
# pythonu nepřeteče integer

def main():
    a = input("Zadej cislo: ")
    b = input("Zadej cislo: ")
    operator = input("Zadej operator: ")

    print(calc(a, b, operator))
    pass


if __name__ == '__main__':
    main()