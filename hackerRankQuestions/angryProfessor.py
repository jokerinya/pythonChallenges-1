"""
Question Link,
https://www.hackerrank.com/challenges/angry-professor/problem
"""

def angryProfessor(k, a):
    on_time = late = 0
    for i in a:
        if i <= 0:
            on_time += 1
        else:
            late += 1
    return "NO" if on_time >= k else "YES"

print(angryProfessor(3, [-1, -3, 4, 2]))  # YES
print(angryProfessor(2, [0, -1, 2, 1]))  # NO