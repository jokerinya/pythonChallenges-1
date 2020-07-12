"""
Task : Write a program that takes a number from the user and 
prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

"""
number = input("Please enter an integer number: ").strip()
check_numbers = [2, 3, 5, 7]
control_list = []
if(number.isdigit()):
    number = int(number)
    if number in check_numbers:
        print(f"Your number {number} is a Prime Number.")
    elif number == 1:
        print(f"Your number {number} is NOT a Prime Number.")
    else:
        for i in check_numbers:
            control_list.append(number % i)
        if False in control_list:
            print(f"Your number {number} is NOT a Prime Number.")
        else:
            print(f"Your number {number} is a Prime Number.")
else:
    print(f"Please provide a integer number.{number} is not an integer ")
