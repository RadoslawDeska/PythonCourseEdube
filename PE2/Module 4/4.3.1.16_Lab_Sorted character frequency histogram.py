'''
Estimated time

15-30 minutes
Level of difficulty

Medium
Prerequisites

4.3.1.15
Objectives

    improve the student's skills in operating with files (reading/writing)
    using lambdas to change the sort order.

Scenario

The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

    the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
    the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:
cBabAa

samplefile.txt

the expected output should look as follows:
a -> 3
b -> 2
c -> 1

output

Tip: Use a lambda to change the sort order.
'''

import os

input_fname = input("Give the file name: ")
directory = os.path.dirname(__file__)

d = {}
try:
    f = open(os.path.join(directory,input_fname), mode="r",encoding="utf-8")
    
    for ch in f.read():
        if ch.isalpha():
            small = ch.lower()
            if small in d.keys():
                d[small] += 1
            else:
                d[small] = 1  
    f.close()

except OSError as e:
    print("Cannot open file due to following reason: ", e)

def key():
    return lambda item: item[1]  # this lambda returns second element of tuple "item"

d_sorted = dict(sorted(d.items(), key=key(), reverse=True))

for ch in d_sorted.keys():
    print(ch, "->", d[ch], sep=" ")