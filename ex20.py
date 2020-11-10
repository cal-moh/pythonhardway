from sys import argv

script, input_file = argv
# f.read() brings in a string element that goes straight to the stdout because of the print function 
def print_all(f):
    print(f.read())
# f.seek() is taking the pointer or whatever it is back to zero, which is the first place.     
def rewind(f):
    f.seek(0)
# This is far more interesting - how do lines get changed here? -- A
# Spent some time with itertools here. Good thing to think about in the future -https://docs.python.org/3/library/itertools.html
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')
# What are the differences between the next two lines
# with open(input_file, 'r') as current_file:
    # print("")
current_file = open(input_file, 'r')
print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
# I think lines get changed here. Attempting to suppress all current_line lines after initial declaration -- A. Clearly, this current_line increment is not working. Will now attempt current_file.seek(arg). So B has yielded interesting results - B has only moved across characters, not lines. 
# Did a few experiments and realised that I will probably need another kind of counter to get to the line that is being requested. Reversing all of Hypothesis B lines
# Style question - ask someone how you end up testing a hypothesis in code
current_line = 1
# current_file.seek(current_line) # -- B
print_a_line(current_line, current_file)
# Testing Hypothesis A -- suppressing current_line increments -- A
current_line += 1 # -- A
# current_line = current_line + 2 # -- B
# current_file.seek(current_line) # -- B
print_a_line(current_line, current_file)
# Testing Hypothesis A -- suppressing current_line increments -- A
current_line += 1 # -- A
# current_line = current_line + 2 # -- B
# current_file.seek(current_line) # -- B
print_a_line(current_line, current_file)

