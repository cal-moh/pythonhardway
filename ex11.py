# end='' suppresses the next line character
print("How old are you?", end='')
# clear input function
age = input()
# input() has a built in print prompt it seems. Also, it strips out the default end-of-line newline character when it reads and writes this. Finally, it converts this to a string
height = input("How tall are you? ")
#height = input()
weight = input("How much do you weigh? ")
# weight = input()
# added units on my own, because why wouldn't you have units.
print(f"So, you're {age} years old, {height} cm tall, and {weight} kg heavy")

# Anything that consumes the output of a function that is compulsorily going to spit out an output, works. In this case, a print function eats as input what the input() throws as output. Don't need to designate a separate variable to store the output of input()   

print(input("Nieman, were you leading, or were you trailing?"))