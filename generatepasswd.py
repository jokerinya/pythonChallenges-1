"""
Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

- Expected Output:

Please enter your full name: StephenClarkson
rto8807

Please enter your full name: BillJames
ils6032

Please enter your full name: MarkJackson
jkr7034

Please enter your full name: CarlSmith
iih7800
"""


from random import randint


def validation(entry):
    empty_values = ("null", "none", "undefined", "false", "true")
    if entry == "" or entry == None:
        return "Invalid input: FullName can not be empty"
    elif entry in empty_values:
        return f"Your entry cannot be special words like {', '.join(empty_values)}."
    elif not entry.isalpha():
        return f"Your entry {entry} cannot contain number, spaces and other special characthers like *,-,_"
    else:
        return "ok"


def produce_passwd(fullname):
    alpha_count = 3  # number of letters in password
    rand_alphas = ''.join([fullname[randint(0, len(fullname)-1)]
                           for i in range(alpha_count)])
    rand_numbers = str(randint(1000, 9999))
    passwd = rand_alphas + rand_numbers
    return passwd


print("Print enter your FullName without spaces and with only with letters. (Exp: JohnDoe, AliceWonder)")
print("For exit the program, please type 'exit'.")
entry = input("Enter FullName: ").strip().lower()
if entry != 'exit':
    while True:
        valid_result = validation(entry)
        if valid_result == "ok":
            print(f"Your password is: {produce_passwd(entry)}")
        else:
            print(valid_result)
        entry = input("Enter FullName('exit' for exiting): ").strip().lower()
        if entry == "exit":
            break
print("Thank you.")
