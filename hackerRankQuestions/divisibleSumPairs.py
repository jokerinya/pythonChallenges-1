"""
Question Link,
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""

def divisibleSumPairs(n, k, ar):
    # let create a variable so we can track the number of pairs that provide questions condition
    counter = 0
    for i in range(n):
        for j in range(i, n):
            # i<j must be sustained, so if they are equal continue that iteration
            if i == j: continue
            # checks the sum of pair is divisible or not
            if (ar[i] + ar[j])%k == 0:
                counter += 1
    return counter

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))  # 5