
"""
Question Link,
https://www.hackerrank.com/challenges/bon-appetit/problem
"""

def bonAppetit(bill, k, b):
    total = sum(bill)
    if total/2 == b:
        # Removes the item Anna didn't eat
        bill.remove(bill[k])
        # calculates Brian should give to Anna
        print(int((total - sum(bill))/2))
        return
    print("Bon Appetit")
