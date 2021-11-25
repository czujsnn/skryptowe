
from inspect import signature

def argumenty(root_args):
    def decoratorFunc(suma): 
        def wrap(*args): 
            nums = [arg for arg in args]
            neededArgs = len(list(signature(suma).parameters))


            if len(nums) + len(root_args) < neededArgs:
                raise TypeError("suma() takes exactly 3 argumetns (2 given)")

            c = 0
            while len(nums) < neededArgs:
                nums.append(root_args[c])
                c += 1

            suma(*nums)

            try:
                return root_args[c]
            except IndexError:
                return None

        return wrap
        
    return decoratorFunc


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def sum(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
    
    def sumWithoutDecorator(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    @argumenty(argumentyRoznica)
    def substraction(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def substractionWithoutDecorator(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def __setitem__(self, name, value):
        if name == "suma":
            self.argumentySuma=value
            self.sum = argumenty(self.argumentySuma)(self.sumWithoutDecorator)

        if name == "roznica":
            self.argumentyRoznica=value
            self.substraction = argumenty(self.argumentyRoznica)(self.substractionWithoutDecorator)

if __name__ == '__main__':
    op = Operacje()
    op.sum(1, 2, 3)  # Wypisze: 1+2+3=6
    op.sum(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.sum(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'

    try:
        op.sum()  # TypeError: suma() takes exactly 3 arguments (2 given)
    except Exception as e:
        print(e)

    op.substraction(2, 1)  # Wypisze: 2-1=1
    op.substraction(2)  # Wypisze: 2-4=-2
    wynik = op.substraction()  # Wypisze: 4-5=-1
    print(wynik)  # Wypisze: 6

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    # oznacza, że   argumentySuma=[1,2]
    print(op.argumentySuma)

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że   argumentyRoznica=[1,2,3]
    print(op.argumentyRoznica)