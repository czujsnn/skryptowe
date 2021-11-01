import lista
import slownik
import sys

if sys.argv[1] == "--lista":
    lista.zapisz()
    lista.wypisz()

if sys.argv[1] == "--slownik":
    slownik.zapisz()
    slownik.wypisz()