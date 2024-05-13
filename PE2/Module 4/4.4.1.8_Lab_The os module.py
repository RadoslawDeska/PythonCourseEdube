'''
Estimated time

15-30 min

Level of difficulty

Easy

Objectives

    improving the student's skills in interacting with the operating system;
    practical use of known functions provided by the os module.

Scenario

It goes without saying that operating systems allow you to search for files and directories. While studying this part of the course, you learned about the functions of the os module, which have everything you need to write a program that will search for directories in a given location.

To make your task easier, we have prepared a test directory structure for you:

tree
|---->c
|     |---->other_courses
|           |---->cpp
|           |---->python
|---->cpp
|     |---->other_courses
|           |---->c
|           |---->python
|---->python
      |---->other_courses
            |---->c
            |---->cpp

Directory structure

Your program should meet the following requirements:

    Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
    The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.

Example input:
path="./tree", dir="python"

Example output:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python

'''

import os
os.chdir(os.path.dirname(__file__))

def find(path, dir):
    for item in os.walk(path):
        if item[0].find(dir) != -1:
            print(item[0])
            item[1][:] = []  # prevent further descending into the branch (for full search of the path, disable this line)

find("./tree", "python")
