"""
Question Link,
https://www.hackerrank.com/challenges/drawing-book/problem
"""

def pageCount(n, p):
    # opens front of the book and page is first page
    if p==1: return 0
    # opens thelast page and the page is the last page
    if (n-p)==1 and p%2==0: return 0
    # opens the page before the last page
    if (n-p)==1 and p%2==1: return 1
    # All other conditions
    if n-p >= p:
        return p//2
    return (n-p)//2


print(pageCount(6, 5))  # 1
print(pageCount(5, 4))  # 0
print(pageCount(10, 6))  # 2