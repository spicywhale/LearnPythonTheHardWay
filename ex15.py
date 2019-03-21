#uses the module argv which allows variables to be entered at the command line
from sys import argv
#sets the variables inputted at the command line to script and filename
script, filename = argv
#sets txt so it will open the file entered at the command line
txt = open(filename)
#prints an fstring
print(f"Here's youre file {filename}: ")
#prints the .txt file that you named at the command line
print(txt.read())

print("Type the file name again:")
#sets file_again to the user input with a > infront
file_again = input("> ")
#sets txt_again to open file_again
txt_again = open(file_again)
#prints txt_again with a read command so it will open the file
print(txt_again.read())