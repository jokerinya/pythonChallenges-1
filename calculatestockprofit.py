"""
Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

Example of different list of stock prices and respective outputs.

List = [75,73,60,100,120,130]
Output = 70
List = [10,20,23,22,17,30]
Output = 20
List = [1,6,19,59,30,60]
Output = 59

"""


def calculate(mylist):
    max_diff = 0
    for i in range(len(mylist)):
        for j in mylist[i:]:
            temp_diff = j - mylist[i]
            if temp_diff > max_diff:
                max_diff = temp_diff
    return max_diff


list_a = [75, 73, 60, 100, 120, 130]  # Output must be 70
list_b = [10, 20, 23, 22, 17, 30]  # Output must be 20
list_c = [1, 6, 19, 59, 30, 60]  # Output must be 59
list_d = [9, 11, 8, 5, 7, 10]  # Output must be 5

print(f"List a profit=> {calculate(list_a)}")
print(f"List b profit=> {calculate(list_b)}")
print(f"List c profit=> {calculate(list_c)}")
print(f"List d profit=> {calculate(list_d)}")
