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
            try:
                value = float(value)
            except ValueError:
                raise ValueError(f"The value provided by the '{key}' key cannot be converted to integer (integer or integer-like string expected).")
    elif not isinstance(value, (int, float)):
        raise TypeError(f"The value provided by the '{key}' key is of invalid type (integer or integer-like string expected).")
    
    if value < 0:
        raise Exception("Negative values are not accepted as arguments to the class.")
    
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
            kwargs.update(dict(zip(MyTime.keys, args)))  # this zips args with keys element by element (shorter list defines the dict size)
            for key,value in kwargs.items():
                value = typecheck(key, value)
                self.__dict__[key] = value
        else:  # if no arguments whatsoever
            kwargs.update(dict(zip(MyTime.keys, [0,0,0])))
            for key,value in kwargs.items():
                value = typecheck(key, value)
                self.__dict__[key] = value
        
        self.__dict__ = self.check_overflow()
        
        self.hours = self.__dict__['hours']
        self.minutes = self.__dict__['minutes']
        self.seconds = self.__dict__['seconds']
    
    def __str__(self):
        if self.seconds < 10:
            return f"{self.hours:02}:{self.minutes:02}:0{self.seconds}"
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds}"
    
    def __add__(self, t):
        '''Add time to current time. If t is instance of the class, add all parameters. Otherwise, add seconds.'''
        self.in_seconds, self_precision = self.check_arg(self)
        t, t_precision = self.check_arg(t)
        
        s = self.in_seconds + t
        new_time = self.to_dictionary(s)
        
        seconds = self.set_precision(self_precision, t_precision, new_time)
        
        return f"{self.isnegative}{new_time['hours']:02}:{new_time['minutes']:02}:"+seconds

    def __mul__(self, t):
        self.in_seconds, self_precision = self.check_arg(self)
        t, t_precision = self.check_arg(t)
        
        new_time = self.to_dictionary(self.to_seconds()*t)
        
        seconds = self.set_precision(self_precision, t_precision, new_time)
        
        return f"{self.isnegative}{new_time['hours']:02}:{new_time['minutes']:02}:"+seconds
        
    def __sub__(self, t):
        if isinstance(t, MyTime):
            t = t.to_seconds()
        '''Reverse the __add__'''
        return self.__add__(-t)
    
    def check_arg(self, arg):
        if isinstance(arg, MyTime):
            arg = arg.to_seconds()
        
        if isinstance(arg, str):
            try:
                arg = float(arg)
            except TypeError:
                raise TypeError(f"Cannot operate on non-numbers: {arg} is of type {type(arg)}")
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Cannot operate on non-numbers: {arg} is of type {type(arg)}")
        
        if isinstance(arg, float):
            arg_precision = self.get_precision(arg)
        else:
            arg_precision = 0
        
        return arg, arg_precision
    
    def check_overflow(self):
        '''Used for proper data presentation'''
        return self.to_dictionary(self.to_seconds())
    
    def get_precision(self, num:int|float):
        if isinstance(num, float):
            return len(str(num)[str(num).find('.')+1:])
        else:
            return 0
    
    def set_precision(self, self_precision, t_precision, new_time):
        '''Used when formatting output strings "seconds" value'''
        if self_precision == 0 and t_precision == 0:
            seconds = str(new_time['seconds'])
        elif self_precision > t_precision:        
            seconds = f"{new_time['seconds']:.{self_precision}f}".rstrip('0').rstrip('.')
        else:
            seconds = f"{new_time['seconds']:.{t_precision}f}".rstrip('0').rstrip('.')
        
        if float(seconds) < 10:
            seconds = "0"+seconds
        
        return seconds
    
    def to_dictionary(self, seconds):
        if seconds < 0:
            self.isnegative = "-"
        else:
            self.isnegative = ""
        if self.isnegative:
            seconds = abs(seconds)
        precision = self.get_precision(seconds)
        dic = {}
        dic['hours'] = int(seconds // 3600)
        dic['minutes'] = int(seconds % 3600 // 60)
        if isinstance(seconds, float):
            dic['seconds'] = float(f"{seconds % 3600 % 60:.{precision}f}")
        else:
            dic['seconds'] = seconds % 3600 % 60
        return dic
    
    def to_seconds(self):
        return self.__dict__['hours']*3600+self.__dict__['minutes']*60+self.__dict__['seconds']

c = MyTime(21,58,50)
d = MyTime(1,45,22)

# ADDITION
print(c,d,sep=" + ",end=" = ")
print(c+d)
print(c,"6322".rjust(len(str(d))),sep=" + ",end=" = ")
print(c+6322)

# SUBTRACTION
print(c,d,sep=" - ",end=" = ")
print(c-d)
print(c,"6322".rjust(len(str(d))),sep=" - ",end=" = ")
print(c-6322)

# MULTIPLICATION
print(c,"2".rjust(len(str(d))),sep=" * ",end=" = ")
print(c*2)

# PRINTS OUT
# 21:58:50 + 01:45:22 = 23:44:12
# 21:58:50 +     6322 = 23:44:12
# 21:58:50 - 01:45:22 = 20:13:28
# 21:58:50 -     6322 = 20:13:28
# 21:58:50 *        2 = 43:57:40