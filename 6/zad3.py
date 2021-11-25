import sys
from functools import reduce

print(len(list(filter( lambda x: int(x)%2==0,reduce(
                       lambda x, y: x + y, list(open(file, 'r').read().replace('\n', ' ').split() for file in sys.argv[1:]
                    )
                )
            )
        )
    )
)
#reduce laczymy wszystkie tablice powstale poprzez zesplitowanie po whitespace plikow z argv, lambda x+y, bo [1] + [2] = [1,2], 
#nastepnie filter aby wszystkie elementy z tablicy ktore daja %2 == True zostaly, tworzymy liste z tego a nastepnie dlugosc listy -> wynik.

#python -c "import sys;from functools import reduce;print(len(list(filter(lambda x: int(x)%2==0,reduce(lambda x, y: x + y, list(open(file, 'r').read().replace('\\n', ' ').split() for file in sys.argv[1:]))))))" plik1.txt plik2.txt
