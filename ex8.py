#assigns the variable
formatter = "{} {} {} {}"
#changes formatter's format to function. This allows me to replace the {} in line 2 with 4 other values, be it lines of text, numbers or values.
#prints formatter with 4 different values
print(formatter.format(1, 2, 3, 4))
#prints formatter with 4 different values
print(formatter.format("one", "two", "three", "four"))
#prints formatter with 4 different values
print(formatter.format(True, False, False, True))
#prints formatter with 4 different values
print(formatter.format(formatter, formatter, formatter, formatter))
#prints formatter with 4 different values
print(formatter.format(
    "I'm just sitting here.",
    "Typing lines of text.",
    "I want an orange.",
    "Banana Phone.",
    ))