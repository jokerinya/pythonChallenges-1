"""
Task : Create a list consisting of Fibonacci numbers from 1 to 55 
using control flow statements.

The desired output is like :
fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""

fibonacci = []
i = 1
total = 1
fibonacci.append(i)
fibonacci.append(total)

while True:
    total = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(total)
    i += 1
    if total >= 55:
        break

print(fibonacci)
