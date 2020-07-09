"""
Task:
Find out if a given number is an "Armstrong Number".
An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. 
Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.

Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values 
then display a warning message to the user.
"""


print("Welcome to Amstrong Number Finding Game")
number = input("Please provide a positive integer number: ").strip()
if (number.isdigit()):
    num_digits_len = len(number)  # number's digits
    number_el = list(number)  # number's each elements
    total = 0
    for el in number_el:
        el = int(el)
        total += el**num_digits_len
    if(int(number) == total):
        print(f"Your number {number}, is an Amstrong Number")
    else:
        print(f"Your number {number}, is not an Amstrong Number")
else:
    print(
        f"{number} -> It is an invalid entry. "
        f"Don't use non-numeric, float, or negative values!"
    )
