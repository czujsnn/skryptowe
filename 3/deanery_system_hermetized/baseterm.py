class BaseTerm():
    def __init__(self, hour: int, minute: int, duration: int = 90):
        self._hour = hour
        self._minute = minute 
        self._duration = duration

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
        self._minute = minute

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def setDuration(self, duration):
        self._duration = duration

    
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

    def getUniqueStartingHours(self):
        return (self._hour, self._minute)