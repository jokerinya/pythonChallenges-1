"""
Question Link,
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

def compareTriplets(a, b):
    alice = bob = 0
    for i in range(3):
        if a[i]==b[i]: continue
        if a[i]>b[i]:
            alice += 1
        else:
            bob += 1
    return [alice, bob]


print(compareTriplets([17, 28, 30], [99, 16, 8]))  # [2, 1]