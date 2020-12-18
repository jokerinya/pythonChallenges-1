"""
- Write a python code that finds the largest number among the 5 numbers given by the user as input.

- It is forbidden to use max() function.  

- Indicate which computational thinking concepts have you used.

- Example for user inputs and respective outputs

Input            Output
------------     ------
1 2 3 4 5         5
67 85 19 39       85

"""


print("###  This program finds the largest number in the 5 (five) numbers given by user ###")

num_list = []

for i in range(5):
    while True:
        num = input(f"Please enter the {i + 1}. number: ")
        if (num.isdecimal()):
            num = int(num)
            num_list.append(num)
            break
        else:
            print("Not Valid Input !!!")


max_el = num_list[0]
for i in num_list:
    if max_el < i:
        max_el = i

print(f"Max number is {max_el}")
