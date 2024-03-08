# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

user_submission = int (input('give me a number between 1 and 12: '))
if 1 <= user_submission <= 12 :
    if user_submission == 1:
        print("January")
    elif user_submission == 2:
        print("February")
    elif user_submission == 3:
        print("March")
    elif user_submission == 4:
        print("April")
    elif user_submission == 5:
        print("May")
    elif user_submission == 6:
        print("June")
    elif user_submission == 7:
        print("July")
    elif user_submission == 8:
        print("August")
    elif user_submission == 9:
        print("September")
    elif user_submission == 10:
        print("October")
    elif user_submission == 11:
        print("November")
    elif user_submission == 12:
        print("December")
else:
    # If the number is not in the range 1 to 12
    print("Reading is fundamental, try again!")