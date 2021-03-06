from day import Day
import re

class Term():

    def __init__(self, hour, minute, duration=90, day=None) -> None:

        self.hour=hour
        self.minute=minute
        self.duration=duration
        self.__day= day
        self.translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}

    def __str__(self) -> str:
        if self.__day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        else:
            return f"{self.translate[self.__day.name]} {self.hour}:{self.minute} [{self.duration}]"

    def getStartTime(self):
        int_minute = int(self.minute)

        if int_minute < 10:

            self.startMinutes = f"0{self.minute}"

        elif int_minute == 0:

            self.startMinutes = f"00"

        return self.startMinutes

    def getEndTime(self):

        int_minute = int(self.minute)
        int_hour = int(self.hour)
        int_duration = int(self.duration)

        overflow_hour = (int_minute + int_duration) // 60
        overflow_minutes = (int_minute + int_duration) %60 
        end_hour = (int_hour + overflow_hour) % 24
        
        if overflow_minutes < 10:
            overflow_minutes = f"0{overflow_minutes}"
        elif overflow_minutes == 0:
            overflow_minutes = f"00"

        end_time = f"{end_hour}:{overflow_minutes}"

        return end_time

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


    def __lt__(self, termin):
        if self.hour < termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute < termin.minute:
                return True
        return False

    def __eq__(self, termin):
        if str(self) == str(termin):
            return True
        return False

    def __le__(self, termin):
        if self < termin or self == termin:
            return True
        return False
    
    def __gt__(self, termin):
        if self.hour > termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute > termin.minute:
                return True
        return False
    
    def __ge__(self, termin):
        if self > termin or self == termin:
            return True
        return False

    def __sub__(self, other):
        return Term(other.hour, other.minute, duration=self.hour*60+self.minute+self.duration-other.hour*60-other.minute)


    def get_date_values(self,date):

        date_dict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12}

        for k in date_dict:
            key_occurence=date.count(k)

            if key_occurence > 0:

                for _ in range(key_occurence):
                    date= re.sub(k,str(date_dict[k]),date)
        
        
        #^\d+?\s\d+\s\d+$
        #^\s\d{1,2}:\d{1,2}\s$
        hours_values = re.findall(r"[0-9]{1,2}:[0-9]{2}",date)
        date_values = re.findall(r"[0-9]{1,2} [0-9]{1,2} [0-9]{4}",date)
        
        

        return [[hours_values[0],date_values[0]],[hours_values[1],date_values[1]]]

    def weekDay(self,year, month, day):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        week   = ['Sunday', 
                'Monday', 
                'Tuesday', 
                'Wednesday', 
                'Thursday',  
                'Friday', 
                'Saturday']
        afterFeb = 1
        if month > 2:
            afterFeb = 0

        aux = year - 1700 - afterFeb
        # dayOfWeek for 1700/1/1 = 5, Friday
        dayOfWeek  = 5
        # partial sum of days betweem current date and 1700/1/1
        dayOfWeek += (aux + afterFeb) * 365                  
        # leap year correction    
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
        # sum monthly and day offsets
        dayOfWeek += offset[month - 1] + (day - 1)               
        dayOfWeek %= 7
        dayOfWeek = round(dayOfWeek)

        return (dayOfWeek)

    #def setTerm(self, hour, minute, duration=90, day=None) -> None:
    def setTerm(self,date):

        parsed_date = self.get_date_values(date)
        hourMinuteFrom = parsed_date[0][0].split(":")
        hourFrom = int(hourMinuteFrom[0])
        minuteFrom = int(hourMinuteFrom[1])
        dateFrom = parsed_date[0][1].split()
        dayFrom = int(dateFrom[0])
        monthFrom = int(dateFrom[1])
        yearFrom = int(dateFrom[2])

        #DATES TO

        hourMinuteTo = parsed_date[1][0].split(":")
        hourTo = int(hourMinuteTo[0])
        minuteTo = int(hourMinuteTo[1])
        dateTo = parsed_date[1][1].split()
        dayTo = int(dateTo[0])
        monthTo = int(dateTo[1])
        yearTo = int(dateTo[2])

        self.duration = abs( (yearTo - yearFrom)*52560 + (monthTo - monthFrom)*43200 + (dayTo - dayFrom)*1440 + (hourTo - hourFrom)*60 + (minuteTo - minuteFrom) )

        newWeekday = self.weekDay(yearFrom,monthFrom,dayFrom)

        days = { 1: Day.MON,
                    2: Day.TUE,
                    3: Day.WED,
                    4: Day.THU,
                    5: Day.FRI,
                    6: Day.SAT,
                    7: Day.SUN,
        }

        self.__day = days[newWeekday]
        self.hour = hourFrom
        self.minute = hourMinuteFrom[1]

date1 = "27 I 2021 8:00 - 28 X 2021 21:00"
date2 = "1 I 2021 11:00 - 1 I 2021 12:59"
term1 = Term(8,30,90,Day.TUE)
term2 = Term(10,30,90,Day.MON)
# print(term1)
# print(term1.setTerm(date1))
# print(term1)


if __name__ == "__main__":
    term1 = Term(8, 30)
    term2 = Term(9, 45, 30)
    term3 = Term(9, 45, 90)
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