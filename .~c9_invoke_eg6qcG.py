from sys import argv 

script, input_file = argv 

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_liner(line_count, f):
    print(line_count, f.readline)
    
curr

print("First let's the whole file: \n")

