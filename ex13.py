# These are called feature sets or modules. Also called libraries
from sys import argv
# read the WYSS section for how to run this
# It's interesting that the assignment of variable happens in a many to one way. 
script, first, second, third = argv
# Also interesting is that the input() function takes in a string
fourth = input("What's your favourite song? ")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your favourite song is ", fourth)
# Also interesting that I can do this as an array of values
print("The script is called:", argv[0])
print("Your first variable is:", argv[1])
print("Your second variable is:", argv[2])
print("Your third variable is:", argv[3])

# Counting in negative from the end results in first, to the last from the end
print(argv[-4])
