#uses the \t escape sequence which indents the line of text that it's attached too
tabby_cat = "\tI'm tabbed in."
#uses the n escape to split the text on the line
persian_cat = "I'm split \non a line."
#uses the double backslash which allows you to use a backslash
blackish_cat = "I'm \\ a \\ cat."
#uses the triple quotes
fat_cat = """

I'll do a list:
\t to tab the text in
\t*Cat food
\t*Fishies  #so if i put a comment in the triple quotes does it print?
\t*Catnip #neat \n\t*Grass
"""
#prints the variables we assigned values to
print(tabby_cat)
print(persian_cat)
print(blackish_cat)
print(fat_cat)