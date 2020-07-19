"""
This snippet actually same as leapYear.py however in this assignment
conditional statements are used.

Task:
Find out if a given year is a "leap" year.

In the Gregorian calendar, three criteria must be taken into account to identify leap years:
The year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is not a leap year; unless...
The year is also evenly divisible by 400. Then it is a leap year.
According to these rules, the years 2000 and 2400 are leap years, 
while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
Write a Python program that prints such as "2020 is a leap year" 
if the given year by the user is a leap year, 
prints such as "2019 is not a leap year" otherwise.

"""

print("Please provide the year in 4 digits, like 2000, 1560,.. etc")
year = input("Please enter a year: ").strip()
if(year.isdigit()):
    year = int(year)

    # means year can be divided by 400, 4, 100; if it is, returns True
    divided_to_400 = not bool(year % 400)
    divided_to_4 = not bool(year % 4)
    divided_to_100 = not bool(year % 100)

    if divided_to_400 or (divided_to_4 and not divided_to_100):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"Your entry ({year}) is not integer value.")
