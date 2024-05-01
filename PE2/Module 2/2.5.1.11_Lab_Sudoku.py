'''
Estimated time

60-90 minutes
Level of difficulty

Hard
Objectives

    improving the student's skills in operating with strings and lists;
    converting strings into lists.

Scenario

As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

    each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
    each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
    each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

If you need more details, you can find them here.

Your task is to write a program which:

    reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
    outputs Yes if the Sudoku is valid, and No otherwise.

Test your code using the data we've provided.
Test data

Sample input:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:
Yes


Sample input:

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:
No
'''

sudoku = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

def check_repetitions(set_of_data):
    for list_of_values in set_of_data:
        for ch in list_of_values:
            # print(f"Checking if {ch} is in {list_of_values[list_of_values.index(ch)+1:]}")
            if ch in list_of_values[list_of_values.index(ch)+1:]:
                return False
    return True

rows = sudoku.split('\n')
for row in rows:
    row = list(row) # this creates list of lists of string items

# rows[row index][column index])

# Create transposed rows to easily read columns:
cols = list(map(list, zip(*rows)))
cols = [''.join(col) for col in cols]

# # Create lists of items in subsquares:
subsquares = [[] for _ in range(9)]

for ri, row in enumerate(rows):
    if ri // 3 == 0:
        subsquares[0].append(row[0:3])
        subsquares[1].append(row[3:6])
        subsquares[2].append(row[6:9])
    elif ri // 3 == 1:
        subsquares[3].append(row[0:3])
        subsquares[4].append(row[3:6])
        subsquares[5].append(row[6:9])
    elif ri // 3 == 2:
        subsquares[6].append(row[0:3])
        subsquares[7].append(row[3:6])
        subsquares[8].append(row[6:9])

subsquares = [''.join(sub) for sub in subsquares]

print("Check rows:")
checksum = check_repetitions(rows)

print("Check columns:")
checksum += check_repetitions(cols)

print("Check subsquares:")
checksum += check_repetitions(subsquares)

if checksum < 3:
    print('No.')
else:
    print('Yes.')