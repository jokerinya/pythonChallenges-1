#  Find and print the length of the longest word.

sentence = input("Enter a sentence: ")
words = sentence.split(" ")
i = 0
max_el = words[0]
while i < len(words):
    if(len(max_el) < len(words[i])):
        max_el = words[i]
    i += 1
print(f"Your sentence is: {sentence}")
print(f"Longest word is {max_el}")


# Guess a number :)
number = 34
input_number = int(input("Guess a number: "))
while input_number != number:
    if (input_number < number):
        print("Incorrect, higher please")
    else:
        print("Incorrect, smaller please")
    input_number = int(input("Guess a number: "))
