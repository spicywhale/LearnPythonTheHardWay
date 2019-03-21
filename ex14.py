#imports the module which uses argv
from sys import argv
#assigns the variables script and user_name to user inputted variables
script, user_name = argv
#sets prompt to '>'
prompt = '>'
#prints statements using the fstring to print variables directly into the string
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
#asks a question and uses the user input as a variable
likes = input(prompt)
#asks a question and uses the user input as a variable#asks a question and uses the user input as a variable
print(f"Where do you live {user_name}?")
lives = input(prompt)
#asks a question and uses the user input as a variable
print("What kind of computer do you have?")
computer = input(prompt)
#prints using a triple quote and uses an fstring
print(f"""
Alright, so you said {likes} about liking me.
You said {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")