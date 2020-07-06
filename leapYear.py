"""
Task:

Find out if a given year is a "leap" year.

In the Gregorian calendar, three criteria must be taken into account to identify leap years:
The year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is not a leap year; unless...
The year is also evenly divisible by 400. Then it is a leap year.
According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
Write a Python program that;
Takes a 4-digit year from the user,
Prints True if the given year by the user is a leap year, prints False otherwise.
"""

print("Welcome leap year finding program!")
print("Please provide the year in 4 digits, like 2000, 1560,.. etc")
year = int(input("Please enter a year: "))
divided_to_400 = not bool(year % 400)  # 0 means year can be divided.
divided_to_four = not bool(year % 4)
divided_to_100 = not bool(year % 100)
leap_year = divided_to_400 or (divided_to_four and not divided_to_100)

print(f"Your year is {year} and leap year status is: {leap_year}")
