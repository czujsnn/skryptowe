from inspect import signature

#dekoratory z argumentami zwracają funkcję, która wykorzystuje funkcje aby zwrócić inną funkcje, więc zwraca normalny dekorator

def argumenty(main_args): #argumenty

    def decorator_of_arguments(sum): #funkcja

        def wrapper_of_arguments(*args):

            nums = [arg for arg in args]
            neededArgs = len(list(signature(sum).parameters))  #we get big list of sum function data, we only need its parameters; and to be specific its length

            if len(nums) + len(main_args) < neededArgs:
                raise TypeError(f"suma() takes exactly {neededArgs-1} arguments ({len(nums)+len(main_args) -1} given)")

            c = 0
            while len(nums) < neededArgs:
                nums.append(main_args[c])
                c += 1

            sum(*nums) #wypakowywanie tablicy

            try:
                return main_args[c]
            except IndexError:
                return None

        return wrapper_of_arguments

    return decorator_of_arguments


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
            self.substraction = argumenty(self.argumentyRoznica)(self.substractionWithoutDecorator) #applying decorator to argumenty
                                                                                                    #with parameters: self.argumentyRoznica
                                                                                                    #then it can be used on substraction w/o decorator 

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
    # oznacza, że argumentySuma=[1,2]
    print(op.argumentySuma)

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że argumentyRoznica=[1,2,3]
    print(op.argumentyRoznica)