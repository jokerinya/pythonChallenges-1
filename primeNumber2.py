"""
Task : Print the prime numbers which are between 1 to entered limit number (n).

Collect all these numbers into a list
The desired output for n=100 :

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]

"""
number = input("Please provide a positive limit number: ").strip()
number = int(number)
will_controlled = list(range(2, number + 1))  # this list will be filtered


def find_primes(i):
    if i == 2 or i == 3 or i == 5 or i == 7:
        return True
    elif not i % 2 or not i % 3 or not i % 5 or not i % 7:
        return False
    else:
        return True


controlled = filter(find_primes, will_controlled)
print(list(controlled))
