'''
Estimated time

30-90 minutes
Level of difficulty

Medium
Objectives

    improve the student's skills in operating with files (reading)
    perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.

Scenario

Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5

samplefile.txt

Your task is to write a program which:

    asks the user for Prof. Jekyll's file name;
    reads the file contents and counts the sum of the received points for each student;
    prints a simple (but sorted) report, just like this one:

Andrew Cox 	 1.5
Anna Boleyn 15.5
John Smith 	 7.0

output

Note:

    your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
    implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

Tip: Use a dictionary to store the students' data.
'''

import os

class StudentsDataException(Exception):
    def __init__(self, message=""):
        Exception.__init__(self, message)

class BadLine(StudentsDataException):
    def __init__(self, message=""):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message="The file is empty"):
        StudentsDataException.__init__(self, message)

def sorting_key(item_no):
    return lambda item: item[item_no]  # this lambda returns item_no element of tuple "item"

input_fname = input("Give the file name: ")
directory = os.path.dirname(__file__)

d = {}

try:
    f = open(os.path.join(directory,input_fname), mode="r",encoding="utf-8")  # possible failure: file not found or access denied
    if not f.read(1):
        raise FileEmpty
    f.seek(0)  # come back to the first line
    
    for i, line in enumerate(f.readlines()):
        data = line.split()
        
        *name, score = data
        key = " ".join(name)
        
        for ch in key:
            if not ch.isalpha() and not ch.isspace():
                raise BadLine(f"Bad line number {i+1}")
        
        if key in d.keys():
            d[key] += float(score)  # if `score` is not convertible to float, raises ValueError
        else:
            d[key] = float(score)  # if `score` is not convertible to float, raises ValueError
        
    d_sorted = dict(sorted(d.items(), key=sorting_key(0), reverse=False))

    for k,v in d_sorted.items():
        print(f"{k}\t{v}")

except FileNotFoundError:
    print("The file doesn't exist")
except PermissionError as e:
    print("Cannot access the file.\n",e)
except FileEmpty as e:
    print(e)
except ValueError:
    print("Score value is not a number")
except BadLine as e:
    print(e)
except StudentsDataException:
    pass
except OSError as e:  # This captures all other OSErrors apart from File Not Found Error and Permission Error
    print("I/O error occurred: ", os.strerr(e.errno))