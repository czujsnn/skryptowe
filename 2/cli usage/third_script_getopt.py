import sys
import getopt
import lista
import slownik

if sys.argv:
    try:
        opt, args = getopt.getopt(sys.argv[1:], '', ['modul='])

        if opt[0][1] == 'lista':
            
            lista.zapisz()
            lista.wypisz()

        elif opt[0][1] == 'slownik':

            slownik.zapisz()
            slownik.wypisz()

    except:
        print('Wrong argument! Try using --modul=lista or --modul=slownik')

else:
    print('Provide at least one argument.')