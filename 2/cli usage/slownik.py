import sys
slownik = {}

print('Ładowanie modułu "{0}"'.format(__name__))

def zapisz():

    for char in sys.argv[2:]:
    
        if char in slownik.keys():
            slownik[char] += 1

        else:
            slownik[char] = 1

def wypisz():

    print('Wywołano funkcję "wypisz()" modułu "{0}"\n'.format(__name__))

    if slownik: 
        for key, value in sorted(slownik.items()):
            print(f'{key}:{value}',end=',')



############################################
print('Załadowano moduł "{0}"'.format(__name__))

if __name__ == "__main__":
    zapisz()
    wypisz()

