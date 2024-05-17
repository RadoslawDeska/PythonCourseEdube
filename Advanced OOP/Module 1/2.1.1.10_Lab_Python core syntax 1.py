'''
Estimated time

30-60 minutes
Level of difficulty

Medium
Objectives

    improving the student's skills in operating with special methods

Scenario

    Create a class representing a time interval;
    the class should implement its own method for addition, subtraction on time interval class objects;
    the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
    check the argument type, and in case of a mismatch, raise a TypeError exception.

'''

def typecheck(key, value):
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"ValueError: The value provided by the '{key}' key cannot be converted to integer (integer or integer-like string expected).")
    elif not isinstance(value, int):
        raise TypeError(f"TypeError: The value provided by the '{key}' key is of invalid type (integer or integer-like string expected).")
    
    return value

class MyTime:
    keys = ['hours', 'minutes', 'seconds']
    
    def __init__(self, *args, **kwargs):
        '''Specify time by providing hours, minutes and seconds argument.
        If you provide any of kwargs, kwargs will be used, otherwise
        If you provide only args, args will be used.
        If you do not provide arguments, defaults to 0 hours, 0 minutes, 0 seconds'''
        
        if kwargs:
            for key in MyTime.keys:
                value = kwargs.get(key, 0)  # Get value provided in kwargs or set default value to 0
                value = typecheck(key, value)
                
                self.__dict__[key] = value  # Rebuild __dict__ if some values were not provided in kwargs
                
        elif args:  # if no keyword argument is passed
            print("No keyword argument passed")
            kwargs.update(dict(zip(MyTime.keys, args)))  # this zips args with keys element by element (shorter list defines the dict size)
            for key,value in kwargs.items():
                value = typecheck(key, value)
                self.__dict__[key] = value
        else:
            print("No argument passed")
            kwargs.update(dict(zip(MyTime.keys, [0,0,0])))
            for key,value in kwargs.items():
                value = typecheck(key, value)
                self.__dict__[key] = value
        
        self.check_overflow(self.__dict__)
        
        self.hours = self.__dict__['hours']
        self.minutes = self.__dict__['minutes']
        self.seconds = self.__dict__['seconds']
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    def __add__(self, t):
        '''Add time to current time. If t is instance of the class, add all parameters. Otherwise, add seconds. Check for overflow'''
        if isinstance(t, MyTime):
            new_sec = self.seconds+t.seconds
            new_min = self.minutes+t.minutes
            new_hrs = self.hours+t.hours
        else:
            new_sec = self.seconds+t
        
        total = MyTime.check_overflow(MyTime,dict(zip(MyTime.keys, [new_hrs,new_min,new_sec])))
            
        return f"{total['hours']:02}:{total['minutes']:02}:{total['seconds']:02}"
    
    def __sub__(self, t):
        pass
    
    def check_overflow(self, dic):
        if dic['seconds'] >= 60:
            dic['minutes'] += 1
            dic['seconds'] -= 60  # what exceeds should be still in seconds
        if dic['minutes'] >= 60:
            dic['hours'] += 1
            dic['minutes'] -= 60  # what exceeds should be still in minutes range
        
        return dic
        
c = MyTime(11,61,59)
d = MyTime(0,0,62)
print(c)
print(d)
print(c+d)