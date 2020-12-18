"""
In this coding challenge, you are going to write a program that takes a string and checks if it contains consecutive vowels or not. It should give `Positive` as an output if it contains consecutive vowels and `Negative` otherwise. For example `saetqi` string contains `a` adjacent to `e`, which means that it contains consecutive vowels. So it should give `Positive` as an output. On the other hand, if you take the string of `statoqag`, the output should be `Negative`.

- Expected Output:

Please enter a string: gasdph
Negative

Please enter a string: aiou
Positive

Please enter a string: taoum
Positive

Please enter a string: a
Negative

"""

vowels = ("a", "e", "i", "o", "u")


def control(el):
    for i in range(len(el)):
        if i+1 == len(el):
            return False
        if (el[i] in vowels) and (el[i+1] in vowels):
            return True
    return False


entry = ""
while entry != "exit":
    entry = input("Enter your word (For quit type 'exit')").strip().lower()
    if entry == "exit":
        break

    if entry.isalpha() == False:
        print("Invalid Entry. (Only one word with letters without space)")
        continue

    print("Positive" if control(entry) else "Negative")
