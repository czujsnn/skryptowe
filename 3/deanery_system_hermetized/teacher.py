from uuid import uuid4

class Teacher(object):
    def __init__(self, imie = None, nazwisko = None):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)