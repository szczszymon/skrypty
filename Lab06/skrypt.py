import sys

dane = sum([open(plik, 'r').read().split() for plik in sys.argv[1:]], [])
parzyste = list(filter(lambda num: int(num) % 2 == 0, dane))

print(len(parzyste))
