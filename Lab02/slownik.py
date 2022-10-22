import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################

slownik = {}


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))

    res = ""

    for key, val in slownik.items():
        if res == "":
            res = f"{key}:{val}"
        else:
            res = f"{res}, {key}:{val}"

    print(res)


def zapisz():
    for _ in sys.argv[1::]:
        for char in _:
            if char.isdigit():
                if char not in slownik:
                    slownik[char] = 1
                else:
                    slownik[char] += 1


############################################
print('Załadowano moduł "{0}"'.format(__name__))
