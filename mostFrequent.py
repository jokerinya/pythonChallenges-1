"""
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
the most frequent number is 3 and it was 4 times repeated
"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
frequencies = {}
for i in set(numbers):  # will not take same element to loop
    # key: element, value: iteration count
    frequencies.update({i: numbers.count(i)})

value_list = list(frequencies.values())
key_list = list(frequencies.keys())

most_iterated_count = max(value_list)
index_most_iterated = value_list.index(most_iterated_count)
most_iterated_el = key_list[index_most_iterated]

print(
    f"the most frequent number is {most_iterated_el} and it was {most_iterated_count} times repeated")
