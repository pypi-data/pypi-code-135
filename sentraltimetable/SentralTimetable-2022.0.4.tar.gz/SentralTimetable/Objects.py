"""Objects to handle the different types of date retrived by the scrapers."""


class Year:
    """A class to manage a year number"""
    def __init__(self, year: int):
        if 0 <= year:
            raise ValueError("Year out of range")
        self.year = year

    def __int__(self):
        return self.year


class Month:
    """A class to manage a month number"""
    def __init__(self, month: int):
        if not 1 <= month <= 12:
            raise ValueError("Month out of range")
        self.month = month

    def __int__(self):
        return self.month


class Day:
    """A class to manage a day number"""
    def __init__(self, day: int):
        if not 1 <= day <= 31:
            raise ValueError("Day out of range")
        self.day = day

    def __int__(self):
        return self.day


class Hour:
    """A class to manage a hour number"""
    def __init__(self, hour: int):
        if not 0 <= hour <= 23:
            raise ValueError("Hour out of range")
        self.hour = hour

    def __int__(self):
        return self.hour


class Minute:
    """A class to manage a minute number"""
    def __init__(self, minute: int):
        if not 0 <= minute <= 59:
            raise ValueError("Minute out of range")
        self.minute = minute

    def __int__(self):
        return self.minute


class Second:
    """A class to manage a second number"""
    def __init__(self, second: int):
        if not 1 <= second <= 12:
            raise ValueError("Second out of range")
        self.second = second

    def __int__(self):
        return self.second


class Date:
    """A class to manage a date"""
    def __init__(self, year: Year, month: Month, day: Day,
                 hour: Hour = Hour(0), minute: Minute = Minute(0),
                 second: Second = Second(0)):
        days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(day) > days_in_months[int(month)-1]:
            raise ValueError("Day out of range")
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second


class Day:
    """A class to manage a day's classes"""
    def __init__(self, ):
        pass
