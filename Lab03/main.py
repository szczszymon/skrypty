from klasa import Klasa

obiekt1 = Klasa(['a', 'b', 'c'])
obiekt2 = Klasa(['x', 'y', 'z'])
print('*' * 30)
print("Po utworzeniu obiektów")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
Klasa.tab = [4, 5, 6]
print("Po wykonaniu instrukcji \u001b[31mKlasa.tab = [4, 5, 6]\u001b[0m'")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print("Po wykonaniu instrukcji \u001b[31mobiekt1.tab = [7, 8, 9]\u001b[0m'")
obiekt1.tab = [7, 8, 9]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print(
    "Po wykonaniu instrukcji '\u001b[31mobiekt2.tab = [-3, -2, -1]\u001b[0m'")
obiekt2.tab = [-3, -2, -1]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('*' * 30)

'''
Pierwsza wersja:

[azerty@colemak Lab03]$ python3 main.py
Załadowano zawartość pliku '/home/azerty/Studia/III Semestr/Programowanie Skryptowe/CWL/Lab03/klasa.py'
Wywołano metodę ::    __init__      obiektu ::140339981729744
Wywołano metodę ::    __init__      obiektu ::140339981729696
******************************
Po utworzeniu obiektów
        Klasa.tab   -> [1, 2, 3]
        obiekt1.tab -> [1, 2, 3]
        obiekt2.tab -> [1, 2, 3]
----------
Po wykonaniu instrukcji Klasa.tab = [4, 5, 6]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> [4, 5, 6]
        obiekt2.tab -> [4, 5, 6]
----------
Po wykonaniu instrukcji obiekt1.tab = [7, 8, 9]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> [7, 8, 9]
        obiekt2.tab -> [4, 5, 6]
----------
Po wykonaniu instrukcji 'obiekt2.tab = [-3, -2, -1]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> [7, 8, 9]
        obiekt2.tab -> [-3, -2, -1]
******************************
Wywołano metodę ::     __del__      obiektu ::140339981729744
Wywołano metodę ::     __del__      obiektu ::140339981729696
[azerty@colemak Lab03]$ 

Obiekty danej klasy dziedziczą jej wartości w tym zainicjowaną własność;
Możemy zmienić wartości własności pojedynczych obiektów danej klasy
'''

'''
Druga wersja:

[azerty@colemak Lab03]$ python3 main.py
Załadowano zawartość pliku '/home/azerty/Studia/III Semestr/Programowanie Skryptowe/CWL/Lab03/klasa.py'
Wywołano metodę ::    __init__      obiektu ::140163434332112
Wywołano metodę ::    __init__      obiektu ::140163434332016
******************************
Po utworzeniu obiektów
        Klasa.tab   -> [1, 2, 3]
        obiekt1.tab -> ['a', 'b', 'c']
        obiekt2.tab -> ['x', 'y', 'z']
----------
Po wykonaniu instrukcji Klasa.tab = [4, 5, 6]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> ['a', 'b', 'c']
        obiekt2.tab -> ['x', 'y', 'z']
----------
Po wykonaniu instrukcji obiekt1.tab = [7, 8, 9]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> [7, 8, 9]
        obiekt2.tab -> ['x', 'y', 'z']
----------
Po wykonaniu instrukcji 'obiekt2.tab = [-3, -2, -1]'
        Klasa.tab   -> [4, 5, 6]
        obiekt1.tab -> [7, 8, 9]
        obiekt2.tab -> [-3, -2, -1]
******************************
Wywołano metodę ::     __del__      obiektu ::140163434332112
Wywołano metodę ::     __del__      obiektu ::140163434332016
[azerty@colemak Lab03]$ 

obiekty zostały zainicjowane wraz z własnością tab, przez co nie dziedziczą wartości tej własności z klasy
'''