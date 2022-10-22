import sys


def isPrime(x):
    if 1 > x:
        return False
    elif x == 1:
        return True

    for _ in range(2, int(x / 2) + 1):
        if x % _ == 0:
            return False
    return True


for param in sys.argv[1::]:
    try:
        if isPrime(int(param)):
            print(param)

    except ValueError:
        pass
