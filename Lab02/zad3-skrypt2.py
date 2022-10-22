import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], '', ["moduł="])

except getopt.GetoptError as err:
    print(err)
    print("Pierwszym argumentem musi być --moduł=lista lub --moduł=slownik !")
    exit(0)

if len(opts) == 0:
    print("Pierwszym argumentem musi być --moduł=lista lub --moduł=slownik !")
    exit(0)

match opts[0][1]:
    case "lista":
        import lista
        lista.zapisz()
        lista.wypisz()

    case "slownik":
        import slownik
        slownik.zapisz()
        slownik.wypisz()

    case _:
        print("Pierwszym argumentem musi być --moduł=lista lub --moduł=slownik !")