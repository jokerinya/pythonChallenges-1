"""
Question Link,
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    # For julian calender, leap year condition
    if year<1918:
        return "12.09." + str(year) if year%4==0 else "13.09." + str(year)
    # For gregorian calendar leap year condition.
    if year%400==0 or year%4==0 and year%100!=0:
        return "12.09." + str(year)
    # Other years
    return "13.09." + str(year)

print(dayOfProgrammer(2001))  # 13.09.2001
print(dayOfProgrammer(1800))  # 12.09.1800