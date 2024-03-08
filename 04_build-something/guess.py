# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:
# Collect user input
word = input("Type something to win: ")
# Convert user input to lowercase
word = word.lower()
# Compare to the string "something"
if word == "something":
# Print a win or lose message
  print("You won... nothing! :)")
else:
  print("You lost :(")
