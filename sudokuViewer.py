"""
Task: The department you work for has received a project that 
displays the solved sudoku puzzles in a digital environment. 

Write a Python code to print out the given sudoku puzzle matrix in the following format.
Given format :
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

Desired output format :
- - - - - - - - - - - - - - - 
0  0  0  | 0  6  4  | 0  0  0  
7  0  0  | 0  0  0  | 3  9  0  
8  0  0  | 0  0  0  | 0  0  0  
- - - - - - - - - - - - - - - 
0  0  0  | 5  0  2  | 0  6  0  
0  8  0  | 4  0  0  | 0  0  0  
3  5  0  | 6  0  0  | 0  7  0  
- - - - - - - - - - - - - - - 
0  0  2  | 0  0  0  | 1  0  3  
0  0  1  | 0  5  9  | 0  0  0  
0  0  0  | 0  0  0  | 7  0  0  
- - - - - - - - - - - - - - -

"""
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
# inserts '|' to arrays
for row in sudoku:
    for i in range(9):
        if i == 3 or i == 7:
            row.insert(i, '|')

# inserts '-' arrays to sudoku
liner = 0
for i in range(13):
    if (liner % 4 == 0):
        sudoku.insert(liner, [15*"- "])
    liner += 1

# adds 2 spaces after sudoku numbers, 1 space after '|'
for row in sudoku:
    for i in range(len(row)):
        if row[i] == [15*"- "]:
            continue
        if row[i] == "|":
            row[i] = str(row[i]) + " "
        else:
            row[i] = str(row[i]) + "  "

# prints the desired output
for row in sudoku:
    for i in row:
        print(i, end="")
    print()
