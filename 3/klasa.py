class Klasa(object):
    tab = [1,2,3]
    def __init__(self, tab, x1, x2):
        self.tab = tab
        self._zmienna1=x1
        self.__zmienna2=x2
        #print(obiekt._Klasa__zmienna2)

        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        print(self.__zmienna2)
        return "Wywołano metodę '__str__()'"

    def __repr__(self):
        return "Wywołano metodę '__repr__()'"

    def metodaInstancyjna(self):
        print("Wywołano metodę 'metodaInstancyjna()'")
        print(f"instance tab = {self.tab}")
        print(f"class tab = {Klasa.tab}")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")

