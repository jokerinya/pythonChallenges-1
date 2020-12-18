"""
Write a function that takes in a list and finds the majority vote inside it. Each letter in the least means an individual vote in favour of that letter. You can use the following list to test your function:

majority_vote(["A", "A", "A", "B", "C", "A"])

- Expected Outputs:

```text
Input: majority_vote(["A", "A", "A", "B", "C", "A"]) 
Output: "A"
"""


def majority_vote(arr):
    results = {i: arr.count(i) for i in set(arr)}

    # return max(results, key=lambda x: results[x])
    return max(results, key=results.get)


print(majority_vote(["A", "A", "A", "B", "C", "A"]))
