
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
           self.day == d2.day

    def tomorrow(self):
        '''Changes calling object to represent the next day'''
        
        if self.month == 12 and self.day == DAYS_IN_MONTH[self.month]:  # Last day of year
            self.month = 1
            self.day = 1
            self.year += 1

        elif self.isLeapYear() and self.month == 2 and self.day == 28:  # Add day to leap Februar
            self.day += 1
            
        elif self.day >= DAYS_IN_MONTH[self.month] or (self.isLeapYear() and self.month == 2 and self.day == 29):  # Last day of month
            self.month += 1
            self.day = 1

        else:
            self.day += 1

    def yesterday(self):
        '''Changes calling object to represent the previous day'''

        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year -= 1

        elif self.isLeapYear() and self.month == 3 and self.day == 1:
            self.month -= 1
            self.day = 29

        elif self.day == 1:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month]

        else:
            self.day -= 1

    def addNDays(self, N):
        '''Assuming N is a non-negative integer, changes calling object to represent
            N days after the original date'''
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''Assuming N is a non-negative integer, changes calling object to represent
            N days before the original date'''
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''Returns True if self occurs before d2, False otherwise'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def isAfter(self, d2):
        '''Returns True if self occurs after d2, False otherwise'''
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month > d2.month:
                return True
            elif self.month == d2.month:
                if self.day > d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def diff(self, d2):
        '''Returns an integer representing the number of days between self and d2'''
        day1 = Date(self.month, self.day, self.year)
        day2 = Date(d2.month, d2.day, d2.year)
        count = 0

        if day1.isBefore(day2):
            while day1.isBefore(day2):
                day1.tomorrow()
                count -= 1
        else:
            while day1.isAfter(day2):
                day1.yesterday()
                count += 1
        return count

    def dow(self):
        '''Returns a string representing the day of the week of the Date object'''
        DAYS_OF_WEEK = ("", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        known = Date(1, 1, 2006)                # Sunday
        count = 1
        days_between = self.diff(known)
        
        if days_between > 0:
            for i in range(days_between):
                if count == 7:
                    count = 1
                else:    
                    count += 1
        else:
            for i in range(abs(days_between)):
                if count == 1:
                    count = 7
                else:
                    count -= 1
        return DAYS_OF_WEEK[count]












    
        
