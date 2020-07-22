"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. 
You are asked to calculate the number of letters or 
any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.
"""
sentence = input("Enter a sentence please: ").strip()
chars = list(set(sentence))
analysis = {i: sentence.count(i) for i in chars}
print(analysis)


# As an extra, also we can sort letter numbers.
sorted_analysis = {k: v for k, v in sorted(
    analysis.items(), key=lambda item: item[1], reverse=True)}
print(sorted_analysis)
