'''
Estimated time

15-30 minutes
Level of difficulty

Easy
Objectives

    improving the student's skills in operating with strings;
    encouraging the student to look for non-obvious solutions.

Scenario

Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

    asks the user for some text;
    checks whether the entered text is a palindrome, and prints result.

Note:

    assume that an empty string isn't a palindrome;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent;
    there are more than a few correct solutions - try to find more than one.

Test your code using the data we've provided.
Test data

Sample input:
Ten animals I slam in a net

Sample output:
It's a palindrome


Sample input:
Eleven animals I slam in a net

Sample output:
It's not a palindrome

'''

text = input('Check for palindrome: ')
if text.isspace():
    print("It's not a palindrome")
else:
    text_nospace = ''.join(text.upper().split(' '))
    text_reversed = text_nospace[::-1]
    
    if text_nospace == text_reversed:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
    