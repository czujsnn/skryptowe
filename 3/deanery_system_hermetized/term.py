from day import Day
import re

class Term():

    def __init__(self, hour, minute, duration=90, day=None) -> None:

        self._hour=hour
        self._minute=minute
        self._duration=duration
        self.__day= day
        self.translate = {"MON":"Poniedziałek","TUE":"Wtorek","WED":"Środa","THU":"Czwartek","FRI":"Piątek","SAT":"Sobota","SUN":"Niedziela"}

    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def setHour(self, hour):
        self._hour = hour

    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def setMinute(self, minute):
        return self._minute

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def setDuration(self, duration):
        self._duration = duration

    @property
    def day(self):
        return self._Term__day

    @day.setter
    def setDay(self, day):
        self._day = day

    def __str__(self) -> str:
        if self.__day == None:
            return f"{self._hour}:{self._minute} [{self._duration}]"
        else:
            return f"{self.translate[self.__day.name]} {self._hour}:{self._minute} [{self._duration}]"
    
    def __repr__(self) -> str:
        if self.__day == None:
            return f"{self._hour}:{self._minute} [{self._duration}]"
        else:
            return f"{self.translate[self.__day.name]} {self._hour}:{self._minute} [{self._duration}]"
                    
    def getStartTime(self):
        int_minute = int(self._minute)

        if int_minute < 10:

            self._startMinutes = f"0{self._minute}"

            return self._startMinutes

        elif int_minute == 0:

            self._startMinutes = f"00"

            return self._startMinutes

        else:

            return self._minute

    def getEndTime(self):

        int_minute = int(self._minute)
        int_hour = int(self._hour)
        int_duration = int(self._duration)

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

    def laterThan(self,term):
        return not self.earlierThan(term)

    def equals(self,term):

        if self.__day.difference(term.__day) == 0 and self._hour == term._hour and self._minute == term._minute:

            return True

        else:

            return False

    def __lt__(self, termin):

        if self._hour < termin._hour:
            return True

        elif self._hour == termin._hour:

            if self._minute < termin._minute:
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

        if self._hour > termin._hour:
            return True

        elif self._hour == termin._hour:

            if self._minute > termin._minute:
                return True

        return False
    
    def __ge__(self, termin):

        if self > termin or self == termin:
            return True

        return False

    def __sub__(self, other):
        return Term(other._hour, other._minute, duration=self._hour*60+self._minute + self._duration - other._hour*60 - other._minute)

    def getStartTime_pr(self):
        return f'{self._hour}:{self._minute}'

    def get_date_values(self,date):

        date_dict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12}

        for k in date_dict:
            key_occurence=date.count(k)

            if key_occurence > 0:

                for _ in range(key_occurence):
                    date= re.sub(k,str(date_dict[k]),date)
        
        hours_values = re.findall(r"[0-9]{1,2}:[0-9]{2}",date)
        date_values = re.findall(r"[0-9]{1,2} [0-9]{1,2} [0-9]{4}",date)
        
        return [[hours_values[0],date_values[0]],[hours_values[1],date_values[1]]]

    def weekDay(self,year, month, day):

        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1

        if month > 2:
            afterFeb = 0

        aux = year - 1700 - afterFeb

        dayOfWeek  = 5
        dayOfWeek += (aux + afterFeb) * 365                  
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
        dayOfWeek += offset[month - 1] + (day - 1)               
        dayOfWeek %= 7

        dayOfWeek = round(dayOfWeek)

        return (dayOfWeek)


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

        self._duration = abs( (yearTo - yearFrom)*52560 + (monthTo - monthFrom)*43200 + (dayTo - dayFrom)*1440 + (hourTo - hourFrom)*60 + (minuteTo - minuteFrom) )

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
        self._hour = hourFrom
        self._minute = hourMinuteFrom[1]


#if __name__ == "__main__":
#    term1 = Term(8, 30)
#    term2 = Term(9, 45, 30)
#    term3 = Term(9, 45, 90)
#    print(term1)                             # Ma się wypisać: "8:30 [90]"
#    print(term2)                             # Ma się wypisać: "9:45 [30]"
#    print(term3)                             # Ma się wypisać: "9:45 [90]"
#    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
#    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
#    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
#    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
#    print("term2 == term2:", term2 == term2) # Ma się wypisać True
#    print("term2 == term3:", term2 == term3) # Ma się wypisać False
#    term4 = term3 - term1                    # Tworzy termin, którego:
#                                            # - godzina rozpoczęcia jest taka jak 'term1',
#                                            # - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
#    print(term4)  

term1 = Term(1,30,90,Day.FRI)
date3 = "5 V 2021 12:40 - 5 V 2021 12:41"
term1.setTerm(date3)

print(type(term1))
values = (term1._hour,term1._minute,term1._duration,term1._Term__day.value)
print(values)

term1 = Term(8,30,1511,Day.TUE)
date2 = "1 I 2021 11:00 - 1 I 2021 12:59"
term1.setTerm(date2)
values = (term1._hour,term1._minute,term1._duration,term1._Term__day.value)
print(values)