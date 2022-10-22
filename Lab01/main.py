from fractions import Fraction


# 1
def sum(arg1, arg2):
    if not isinstance(arg1, complex) and not isinstance(arg1, Fraction):
        arg1 = float(arg1)

    if not isinstance(arg2, complex) and not isinstance(arg2, Fraction):
        arg2 = float(arg2)

    return arg1 + arg2


# 2 - 5
# print(f"suma = {sum(2, 2)}")
# print(f"suma = {sum(2, 2.0)}")
# print(f"suma = {sum(2, '2')}")  # Typowanie silne, dynamiczne
#
# zmienna = 2
# print(type(zmienna))
#
# zmienna = '2'
# print(type(zmienna))

# 6 - 8
# print(f"__name__ = {__name__}")  # nazwa to __main__, po imporcie to main

# 9
if __name__ == "__main__":
    print(f"suma = {sum(2, 2)} (skrypt uruchomiony bezpośrednio)")
