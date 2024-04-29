'''
Objectives

    improving the student's skills in operating with strings;
    using strings to represent non-text data.

Scenario

You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.
Test data

Sample input:
123

Sample output:
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Sample input:
9081726354

Sample output:
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
'''

def display(digits, s="#"):
    for i in range(5):
        for digit in digits:
            match digit:
                case '1':
                    print(one(s), end='')
                case '2':
                    print(two(i,s), end='')
                case '3':
                    print(three(i,s), end='')
                case '4':
                    print(four(i,s), end='')
                case '5':
                    print(five(i,s), end='')
                case '6':
                    print(six(i,s), end='')
                case '7':
                    print(seven(i,s), end='')
                case '8':
                    print(eight(i,s), end='')
                case '9':
                    print(nine(i,s), end='')
                case '0':
                    print(zero(i,s), end='')
        print('')
        
def one(s):
    return '  {s} '.format(s=s)

def two(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case 1:
            return '  {s} '.format(s=s)
        case 3:
            return '{s}   '.format(s=s)

def three(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case _ if i in [1,3]:
            return '  {s} '.format(s=s)

def four(i,s):
    match i:
        case _ if i in [0,1]:
            return '{s} {s} '.format(s=s)
        case 2:
            return '{s}{s}{s} '.format(s=s)
        case _ if i in [3,4]:
            return '  {s} '.format(s=s)

def five(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case 1:
            return '{s}   '.format(s=s)
        case 3:
            return '  {s} '.format(s=s)

def six(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case 1:
            return '{s}   '.format(s=s)
        case 3:
            return '{s} {s} '.format(s=s)

def seven(i,s):
    match i:
        case 0:
            return '{s}{s}{s} '.format(s=s)
        case _ if i in range(1,5):
            return '  {s} '.format(s=s)

def eight(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case _ if i in [1,3]:
            return '{s} {s} '.format(s=s)

def nine(i,s):
    match i:
        case _ if i in [0,2,4]:
            return '{s}{s}{s} '.format(s=s)
        case 1:
            return '{s} {s} '.format(s=s)
        case 3:
            return '  {s} '.format(s=s)

def zero(i,s):
    match i:
        case 0 | 4:
            return '{s}{s}{s} '.format(s=s)
        case _ if i in range(1,4):
            return '{s} {s} '.format(s=s)

display('0123456789','*')
