"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""
# According to the problem statement, x2 is always bigger than x1
def kangaroo(x1, v1, x2, v2):
    # Check if already there is a chance to catch the kangroo on the front
    if v2 >= v1:
        return "NO"
    # totaldistance = jumpcount * jumpdistance + starting position
    # According to the upper equation totaldistances and jumpcount must be same
    # j*v2 + x2 = j*v1 + x1 
    # y = (x1-x2) / (v2-v1)     ----> y must be an integer. so that is why we use modulus operator
    if (x1 - x2) % (v2 - v1) == 0:  # means integer
        return "YES"
    else:
        return "NO"

print(kangaroo(43, 2, 70, 2))  # NO
print(kangaroo(0, 3, 4, 2))  # YES

# Alternatively, a while loop solution can be made, but this solution is more consice.