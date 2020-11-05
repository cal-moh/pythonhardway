# Functions are pieces of named code (like variables are named values). These take in arguments like argv does. 
# this one is like your scripts with argv
# Can only supply as many arguments as the inside of the function is processing - the asterik can't mean endless arguments. Also, the * indicates that this is going to be a list
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1:{arg1}, arg2:{arg2}")
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("George", "RR", "Martin")
print_two_again("Chris", "Martin")
print_one("Chris")
# Can't supply an argument to something that doesn't take arguments. Wonder if there's a way to indicate this while writing code itself. I guess this is what IDEs do
print_none()