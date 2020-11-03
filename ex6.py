types_of_people = 10
# Formatting can be declared for variable strings at the initialisation or assignment stage itself 
x = f"There are {types_of_people} types of people."

binary = "binary"
# The apostrophe functions as a string character and not as a special signifier like the double quotation mark, or a string initiator 
do_not = "don't"
# Confirmation that a single formatting f can take care of multiple variables inside
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
# A string variable can also be added to another string print
print(f"I said: {x}")
# Interesting how within the outermost double quotes, I can use any number of single quotes inside, including a pair
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny!? {}"
#Interesting - this adds the f"" thing later, by using a string's native formatting function, and picking up the curly braces. Inputs the variable as an input to the format. What if I get rid of the curly braces? Function still works - the input is optional.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# Clearly, adding of strings like this results in a concatenate
print(w + e)