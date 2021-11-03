import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################

lista = []

lista = ["" for x in range(0,10)]


def get_digits(num):
    digits = []

    if num < 10:

        digits.append(num)
    
    else:

        get_digits(num // 10)
        digits.append(num%10)

    return digits


def zapisz():

    for arg in sys.argv[2:]:
        
        if len(arg) >1:

            for digit in arg:
                
                digit = str(digit)
                list_index = int(digit)
                current_element = lista[list_index]
                current_element += digit
                lista[list_index] = current_element

        else:
            
            list_index = int(arg)
            current_element = lista[list_index]
            current_element += arg
            lista[list_index] = current_element
                                    
                                                                      #|
    while "" in lista:                     #remove that, and uncomment v to have desired output which is described below.
        lista.remove("")

def wypisz():

    print('\nWywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for number in range(len(lista)):


        #if lista[number] == "":
        #    print(lista)                   THIS IS OPTIONAL TO HAVE OUTPUT LIKE 0:0,1:0, when number isnt' appearing in arg input.
        #    print(f"{number}:0",end=",")
        #
        #else:

            same_number=list(lista[number])
            number_count = same_number.count(lista[number][0])
            print(f"{lista[number][0]}:{number_count}",end=",")

    

print('Załadowano moduł "{0}"'.format(__name__))

if __name__ == "__main__":
    zapisz()
    wypisz()