# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.



hunger = input('how hungary are you?\n' )
hunger = int (hunger)

if hunger >= 2 :
    print("Eat the pizza")
elif hunger < 2:
    print("Eat the apple")
else:
    print("Don't eat anything")
