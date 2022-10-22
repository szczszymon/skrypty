lancuch1 = '''Pierwszy
Wielolinijkowy
Tekst
w
języku
polskim
'''

lancuch2 = '''Drugi
tekst
kodowanie
UTF-8
ąąśśęęęććóółłżżźźź
'''

print((lancuch1 + lancuch2) * 3)


lancuch = 'Dowolny tekst na potrzeby zadania pierwszego zestawu drugiego'

print(lancuch[0])

print(lancuch[:2])

print(lancuch[2:])

print(lancuch[-2])

print(lancuch[-3:])

print(lancuch[0::2])


# lancuch[3] = 'Z'      # Nie mogą być modyfikowane -> Object does not support item assignment
