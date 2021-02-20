"""
Question Link,
https://www.hackerrank.com/challenges/sock-merchant/problem
"""

def sockMerchant(n, ar):
    # finds the uniqe items by converting array to a set
    set_list = set(ar)
    counter = 0
    for i in set_list:
        item_count = ar.count(i)
        # add pair numbers to counter by floor division
        counter += (item_count//2)
    return counter 
