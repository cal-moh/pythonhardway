i = 0
numbers = []
maximum_value = 23
increment = 2

def print_loop(k, increment):
    print(f"At the top i is {k}")
    numbers.append(k)
    
    k = k + increment
    # Interesting idea 1 - the formatting statement lets us print lists too, not sure why the book didn't give out this example
    print(f"Numbers now: {numbers}")#, numbers)
    # I realise now why this has a statement about a line being printed at the top and at the bottom. 
    print(f"At the bottom i is {k}")   
    return k

while i < maximum_value: 
    i = print_loop(i, increment)
    
print("The numbers: ")
# Interesting - paranthesis will not work on any code block initiator it seems (in python)
for num in numbers:
    print(num)