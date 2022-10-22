import sys

if len(sys.argv) < 2:
    print("Pierwszym argumentem musi być --lista lub --slownik !")
    exit(0)

match sys.argv[1]:
    case "--lista":
        import lista
        lista.zapisz()
        lista.wypisz()

    case "--slownik":
        import slownik
        slownik.zapisz()
        slownik.wypisz()

    case _:
        print("Pierwszym argumentem musi być --lista lub --slownik !")
