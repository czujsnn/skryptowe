from day import Day

class Term():

    def __init__(self, day, hour, minute,duration) -> None:

        self.hour=hour
        self.minute=minute
        self.duration=duration
        self.__day= day
        self.translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela",}

    def __str__(self) -> str:

        return f"{self.translate[self.__day.name]} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self,term):  

        day_difference = self.__day.difference(term.__day)

        if day_difference > 0:

            return True

        elif day_difference == 0:

            if self.hour < term.hour:
                return True
            
            elif self.hour == term.hour:

                if self.minute < term.minute:
                    return True

            else:
                return False

        else:

            return False

        pass

    def laterThan(self,term):
        return not self.earlierThan(term)

    def equals(self,term):

        if self.__day.difference(term.__day) == 0 and self.hour == term.hour and self.minute == term.minute:

            return True

        else:

            return False

if __name__ == "__main__":
    # term1 = Term(Day.TUE, 9, 45)
    # print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
    # term2 = Term(Day.WED, 10, 15)
    # print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
    # print(term1.earlierThan(term2)); # Ma się wypisać: "True"
    # print(term1.laterThan(term2));   # Ma się wypisać: "False"
    # print(term1.equals(term2));      # Ma się wypisać: "False"

    term1 = Term("",8, 30, 90)
    term2 = Term("",9, 45, 30)
    term3 = Term("",9, 45, 90)
    print(term1)                             # Ma się wypisać: "8:30 [90]"
    print(term2)                             # Ma się wypisać: "9:45 [30]"
    print(term3)                             # Ma się wypisać: "9:45 [90]"
    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
    print("term2 == term2:", term2 == term2) # Ma się wypisać True
    print("term2 == term3:", term2 == term3) # Ma się wypisać False
    term4 = term3 - term1                    # Tworzy termin, którego:
                                            # - godzina rozpoczęcia jest taka jak 'term1',
                                            # - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
    print(term4)  