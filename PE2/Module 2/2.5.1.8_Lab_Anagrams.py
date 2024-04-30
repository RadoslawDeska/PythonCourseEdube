'''
Estimated time

30-60 minutes
Level of difficulty

Easy
Objectives

    improving the student's skills in operating with strings;
    converting strings into lists, and vice versa.

Scenario

An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

    asks the user for two separate texts;
    checks whether, the entered texts are anagrams and prints the result.

Note:

    assume that two empty strings are not anagrams;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent

Test your code using the data we've provided.
Test data

Sample input:
Listen
Silent

Sample output:
Anagrams


Sample input:
modern
norman

Sample output:
Not anagrams

'''

text1 = input('First string: ')
text2 = input('Second string: ')

if not text1 and not text2:
    print('Not anagrams')
elif len(text1) != len(text2):
    print('Not anagrams')
else:
    t1 = sorted(text1.upper())
    t2 = sorted(text2.upper())
    
    compared = [c1==c2 for c1,c2 in zip(t1,t2)]
    
    if all(compared):
        print('Anagrams')
    else:
        print("Not anagrams")
