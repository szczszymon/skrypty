import sys
##################################


def methodBody(self, name):
    return "Wywołano metodę \033[{color}m{name:^17}\033[0m obiektu \033[{color}m{objectId}\033[0m".format(
            name     = name,
            color    = "38:5:{}".format(id(self) % 13 + 1),
            objectId = id(self)
        )
##################################


class Klasa(object):
    tab = [1, 2, 3]

    def __init__(self, wart, arg2, arg3):
        print(methodBody(self, sys._getframe().f_code.co_name))
        self.tab = wart
        self._zmienna1 = arg2
        self.__zmienna2 = arg3

    def __del__(self):
        print(methodBody(self, sys._getframe().f_code.co_name))

    def __str__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def __repr__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def metodaInstancyjna(self):
        print(methodBody(self, sys._getframe().f_code.co_name))
        print(Klasa.tab)
        print(self.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = cls.__name__)
        )

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = __class__.__name__)
        )
##################################


print("Załadowano zawartość pliku '{name}'".format(name=__file__))


'''
[azerty@colemak Lab03]$ python3 -i klasa.py
Załadowano zawartość pliku '/home/azerty/Studia/III Semestr/Programowanie Skryptowe/CWL/Lab03/klasa.py'
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
[azerty@colemak Lab03]$ clear
[azerty@colemak Lab03]$ python3 -i klasa.py
Załadowano zawartość pliku '/home/azerty/Studia/III Semestr/Programowanie Skryptowe/CWL/Lab03/klasa.py'
>>> obiekt = Klasa()
Wywołano metodę ::    __init__      obiektu ::140364113050592
>>> obiekt = None
Wywołano metodę ::     __del__      obiektu ::140364113050592
>>> obiekt = Klasa()
Wywołano metodę ::    __init__      obiektu ::140364113041136
>>> obiekt = Klasa()
Wywołano metodę ::    __init__      obiektu ::140364113050400
Wywołano metodę ::     __del__      obiektu ::140364113041136
>>> obiekt
Wywołano metodę ::    __repr__      obiektu ::140364113050400
>>> print(obiekt)
Wywołano metodę ::     __str__      obiektu ::140364113050400
>>> obiekt.metodaInstancyjna()
Wywołano metodę ::metodaInstancyjna obiektu ::140364113050400
>>> Klasa.metodaKlasowa()
Wywołano metodę   metodaKlasowa   klasy   Klasa
>>> Klasa.metodaStatyczna()
Wywołano metodę  metodaStatyczna  klasy   Klasa
>>> exit()
Wywołano metodę ::     __del__      obiektu ::140364113050400
[azerty@colemak Lab03]$ 
'''

'''
Zmiana metody Instancyjnej:


[azerty@colemak Lab03]$ python3 -i klasa.py
Załadowano zawartość pliku '/home/azerty/Studia/III Semestr/Programowanie Skryptowe/CWL/Lab03/klasa.py'
>>> obiekt = Klasa([4, 5, 6], 10, 20)
Wywołano metodę ::    __init__      obiektu ::139735367096432
>>> print(obiekt.tab)
[4, 5, 6]
>>> print(obiekt._zmienna1)
10
>>> print(obiekt.__zmienna2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Klasa' object has no attribute '__zmienna2'. Did you mean: '_zmienna1'?
>>> 

>>> print(obiekt._Klasa__zmienna2)
20
>>> 

'''