import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################

lista = []


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))

    res = ""

    for el in lista:
        if res == "":
            res = f"{el[0]}:{el[1]}"
        else:
            res = f"{res}, {el[0]}:{el[1]}"

    print(res)


def zapisz():
    for x in sys.argv[1::]:
        for char in x:
            if char.isdigit():
                for _ in range(len(lista)):
                    if lista[_][0] == int(char):
                        lista[_] = (int(char), lista[_][1] + 1)
                        break
                else:
                    lista.append((int(char), 1))


############################################
print('Załadowano moduł "{0}"'.format(__name__))

'''
# 4
>>> import lista
Ładowanie modułu "lista"
Załadowano moduł "lista"
>>> import lista
>>> import slownik
Ładowanie modułu "slownik"
Załadowano moduł "slownik"
>>> import slownik
>>> lista.wypisz()
Wywołano funkcję "wypisz()" modułu "lista"
>>> slownik.wypisz()
Wywołano funkcję "wypisz()" modułu "slownik"
'''