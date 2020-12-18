"""
- Write a program that creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

- There should be 4 options available to the user and from the options, users should be able to add, find, delete contacts, or terminate the program as shown below.

- Phonebook has users and their corresponding phone numbers.

- At the beginning of the program the phonebook will be empty and user can choose to add new contacts to the phonebook.

- Program should ask user for the input, after giving information text shown as below.

Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :


- Application should be case sensitive and run until the user types `4`.

- Example for user inputs and respective outputs

Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : John
Insert phone number of the person: ten
Invalid input format, cancelling operation ...

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : Alex
Insert phone number of the person: 1234
Phone number of Alex is inserted into the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
1234

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 3
Whom to delete from phonebook : Alex
Alex is deleted from the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
Couldn't find phone number of Alex

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 4
Exiting Phonebook
"""


def finding():
    name = input("Find the phone number of :")
    if name in phone_book.keys():
        print(phone_book[name])
    else:
        print(f"Couldn't find phone number of {name}")


def adding():
    name = input("Insert name of the person : ")
    tel = input("Insert phone number of the person: ")
    if tel.isdecimal():
        phone_book[name] = tel
        print(f"Phone number of {name} is inserted into the phonebook")
    else:
        print("Invalid input format, cancelling operation ...")


def deleting():
    name = input("Whom to delete from phonebook :")
    if name in phone_book.keys():
        del phone_book[name]
    else:
        print(f"Couldn't find phone number of {name}")


def selection_spread(selection):
    if selection == 1:
        finding()
    if selection == 2:
        adding()
    if selection == 3:
        deleting()
    if selection == 4:
        print("Exiting Phonebook")


print("Welcome to Phonebook APP")
phone_book = {}
selection = None
while selection != 4:
    while phone_book == {}:  # first opening; and phonebook empty
        print("It seems your Phonebook is empty. Let's add some info")
        selection = input(
            "Press 2 for adding new number or press 4 for exiting the program: ").strip()
        if selection.isdecimal() and (int(selection) == 4 or int(selection) == 2):
            selection = int(selection)
            if selection == 4:
                selection_spread(selection)
                break
            if selection == 2:
                selection_spread(selection)
        else:
            print("Invalid entry")
    if selection == 4:
        break  # check for empty phonebook exit

    selection = input(
        " 1. Find phone number \n 2. Insert a phone number \n 3. Delete a person from the phonebook \n 4. Terminate \n Select operation on Phonebook App (1/2/3) : ").strip()
    if selection.isdecimal() and (int(selection) in range(1, 5)):
        selection = int(selection)
        selection_spread(selection)
