import re

hour=9
minute=45
duration=90
date1 = "27 I 2021 8:00 - 28 X 2021 21:00"

def get_date_values(date):

    date_dict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12}
    
    for k in date_dict:
        date = re.sub(k,str(date_dict[k]),date)

    # for k in date_dict:
    #     key_occurence=date.count(k)
    #     print(key_occurence)
    #     if key_occurence > 0:

    #         for _ in range(key_occurence):
    #             date= re.sub(k,str(date_dict[k]),date)
    
    print(date,"DATEE")
    #^\d+?\s\d+\s\d+$
    #^\s\d{1,2}:\d{1,2}\s$
    hours_values = re.findall(r"[0-9]{1,2}:[0-9]{2}",date)
    date_values = re.findall(r"[0-9]{1,2} [0-9]{1,2} [0-9]{4}",date)
    print(hours_values,"HOURSVALUEEEES")
    print(date_values,"VALUEEES")
    

    return [[hours_values[0],date_values[0]],[hours_values[1],date_values[1]]]


#print(get_date_values(date1))
#print(get_date_values(date1))
date2 = "10 I 2021 1:00 - 11 V 2021 2:00"
print(get_date_values(date2))

def weekDay(year, month, day):
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

