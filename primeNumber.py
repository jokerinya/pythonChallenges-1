"""
Task : Write a program that takes a number from the user and 
prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

"""
number = input("Please enter an integer number: ").strip()

if(number.isdigit()):
    number = int(number)
    if(number<=1):
        print(f"Your number {number} is NOT a Prime Number.")
    elif(number%2 == 0):
        print(f"Your number {number} is NOT a Prime Number.")
    else:
        for i in range(2, number//2 + 1):
            if(number%i==0):
                print(f"Your number {number} is NOT a Prime Number.")
                break
        else:
            print(f"Your number {number} is a Prime Number.")
else:
    print(f"Please provide a integer number.{number} is not an integer ")
