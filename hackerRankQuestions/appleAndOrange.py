"""
Question Link,
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    right_side_apples = [i+a for i in apples if i > 0]
    left_side_oranges = [i+b for i in oranges if i < 0]
    apple_counter = orange_counter = 0
    for i in right_side_apples:
        if s<=i<=t:
            apple_counter += 1
    for i in left_side_oranges:
        if s<=i<=t:
            orange_counter += 1
    print(apple_counter)
    print(orange_counter)

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
# Output
# 1
# 1
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
# Output
# 1
# 2