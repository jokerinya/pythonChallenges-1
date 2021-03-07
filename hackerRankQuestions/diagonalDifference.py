"""
Question Link,
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

def diagonalDifference(arr):
    # Left to right and Right to left diagram base variables.
    left = right = 0
    length = len(arr)
    index = length -1
    # Left to right sum
    for i in range(length):
        left += arr[i][i]
    # Right to left sum
    for i in range(length):
        right += arr[i][index]
        # Decrease index for next loop execution to one item left.
        index -= 1
    return abs(left - right)