'''
Estimated time

30-60 minutes
Level of difficulty

Easy
Objectives

    Improving the student's skills in using the Calendar class.

Scenario

During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

    Create a class called MyCalendar that extends the Calendar class;
    create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
    in your implementation, use the monthdays2calendar method of the Calendar class.

The following are the expected results:

Sample arguments

year=2019, weekday=0

Expected output

52

Sample arguments

year=2000, weekday=6

Expected output

53
'''
import calendar
from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self, firstweekday=0):
        Calendar.__init__(self, firstweekday)
    
    def count_weekday_in_year(self, year: int, weekday: int):
        if weekday not in range(7):
            return f"{weekday} is not a weekday (expected value: 0-6)"
        
        weeks = 0
        for month in range(1,13):
            for data in Calendar.monthdays2calendar(self, year, month):
                for (day, wkday) in data:
                    if day != 0 and wkday==weekday:
                        weeks += 1
                        
        return f"In {year} {calendar.day_name[weekday]} occurs {weeks} times."
    
    def count_weekday_in_year_v2(self, year, weekday):
        ''' Solution from user `SzyMar3` on Edube.org '''
        return sum(
            1
            for month in range(1, 13)
            for week_list in self.monthdays2calendar(year, month)
            for day_tuple in week_list
            if day_tuple[0] > 0 and day_tuple[1] == weekday
        )
    
c = MyCalendar()
print(c.count_weekday_in_year(2000,calendar.MONDAY))
