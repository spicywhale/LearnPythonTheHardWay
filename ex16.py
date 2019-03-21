#imports argv
from sys import argv
#assigns script and filename to argv
script, filename = argv
#prints strings which provide instructions
print(f"We're going to erase {filename}.")
print("If you dont want to do that, hit CTRL-C (^C).")
print("If you want to do that, hit RETURN")
#waits for an input, but also prints a question mark
input("?")

print("Opening the file")
#opens the target file
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#
target.truncate()

print("Now im gonna ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally we close it.")
target.close()