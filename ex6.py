#assigns a value of ten to the variable types_of_people
types_of_people = 10
#assigns a line of text to the variable x. this text has the variable types_of_people embedded
x = f"There are {types_of_people} types of people."

#assigns the word binary to the variable binary
binary = "binary"
#assigns the word don't to the variable do_not
do_not = "don't"
#assigns a line of text to the variable y with variables binary and do_not embedded
y = f"Those who know {binary} and those who {do_not}."

#prints the variable x
print(x)
#prints the variable y
print(y)

#prints a line of text with x embedded
print(f"I said: {x}")
#prints a line of text with y embedded
print(f"I also said: {y}")

#assigns the word false to the variable hilarious
hilarious = False
#assigns a line of text to the variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"
#prints the variable joke_evaluation and formats hilarious with the .format command
print(joke_evaluation .format(hilarious))
#assigns the variables w and e with lines of text
w = "This is the left side of..."
e = "a string with a right side."
#prints variables w and e
print(w + e)