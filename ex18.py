#this is like one of your scripts with argv
#defines a function, print_two
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#defines another function without the use of *args
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#defines a function with one argument
#this jsut takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
#defines a function with no arguments
#this one takes no arguments
def print_none():
    print("I got nothin'.")

#calls the functions on different strings
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()