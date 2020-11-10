def add(a, b):
    print(f"Adding {a} + {b}")
# Noting that return operations don't need a pair of parantheses. However, I feel more comfortable adding these for readability, as well as avoiding errors. Noting the confusion here on this link - return is a (statement) keyword, even if a return() is used. NOT A FUNCTION. The link also contains reference to official documentation, which states that there is no difference between parantheses, and parantheses-less statements https://stackoverflow.com/questions/22988640/what-is-the-difference-between-return-and-return    
# return is not even a statement, it is a keyword. Discussion here -https://stackoverflow.com/questions/23034078/what-is-the-difference-between-a-statement-and-a-keyword
    return a + b 

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b
# I'd forgotten the colon marks here    
def multiply(a, b):
    print(f"Multiplying {a} x {b}")
    return a * b
# I'd forgotten the colon marks here
def divide(a, b):
    print(f"Dividing {a} / {b}")
    return (a / b)
# I want to start adding this before most command display lines so that it is easily visible on the command line
print("=====================================")
    
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}\n")


#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "\n", "Can you do it by hand?")