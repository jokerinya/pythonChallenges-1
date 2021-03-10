"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""


def plusMinus(arr):
    length = len(arr)
    zero = big = small = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            big += 1
        else:
            small += 1
    # print("{:.6f}".format(big/length))
    # print("{:.6f}".format(small/length))
    # print("{:.6f}".format(zero/length))
    # HackerRank python version is not suitable for below f string type
    # For HackerRank use upper print statements
    print(f"{big/length:.6f}", f"{small/length:.6f}", f"{zero/length:.6f}", sep="\n")


plusMinus([-4, 3, -9, 0, 4, 1])  # 0.500000 0.333333 0.166667