"""
Question Link,
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
"""

def beautifulDays(i, j, k):
    days = 0
    # Add 1 to j because range func doesn't take the limit element
    for d in range(i, j + 1):
        # reverses the number
        rev = int(str(d)[::-1])
        # checks if it is a beatufil day or not
        if abs(d-rev) % k == 0:
            days += 1
    return days