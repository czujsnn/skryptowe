import sys
from collections import Counter

print(dict(sorted(Counter([len(x) for x in sys.stdin.read().split()]).items()))) 

#tworzymy liste z inputu, splitujac po whitespace, bierzemy ich dlugosc, nastepnie tworzymy Counter ktory sluzy do zliczania haszowalnych itemow
#nastepnie wywolujemy metode sorted, dajac obiekt iterowalny counter, i wlasne itemsy(), potem posortowany counter konwertujemy na dict.