"""
Write a function that takes in an input from the user as a parameter for the side length of the square box and draws it to the screen using hashtags ("#").

- Expected Outputs:

Please enter the side length of the box: 4
####
#  #
#  #
####

Please enter the side length of the box: 2
##
##

Please enter the side length of the box: 1
#
"""


while True:
    try:
        a = int(input("Enter decimal number: ").strip())
        if a == 1:
            print(a*"#")
        else:
            print(a*"# ")
            for _ in range(a-2):
                print("# " + "  "*(a-2)+"#")
            print(a*"# ")
        break
    except:
        print("Invalid entry")
