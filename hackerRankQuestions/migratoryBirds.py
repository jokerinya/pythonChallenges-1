"""
https://www.hackerrank.com/challenges/migratory-birds/problem
"""
# According to the problem statement, arr is consist of 1, 2, 3, 4 and 5.
# At core, the problem wants user to find the most frequent element.
def migratoryBirds(arr):
    my_count = {}
    for i in range(1,6):
        my_count[i] = arr.count(i)
    # my_count dictinary: element in array as key and counts of it as value
    return(max(my_count, key=my_count.get))  # max elements

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))  # 3