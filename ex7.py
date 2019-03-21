print("Mary had a little lamb.")
#prints a line of text and uses the .format command to add more text in
print("It's fleece was as {}.".format('snow'))
print("And everywhere that mary went.")
#prints the period 10 times over
print("." * 10) #what'd that do? #it printed the text 10 times
#the next twelve lines assign a lettter to a variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what happens
#without the comma the syntax is invalid
#uses the vriables to print lines of text. since there is a plus the letters assigned to each variable are together
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)