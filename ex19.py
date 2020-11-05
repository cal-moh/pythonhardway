from sys import argv

# Raises an interesting question - do you write functions first, or do you write code first? My guess is you write pseudocode, and then iterate on it till all the repeatable components have made their way into functions. Then you write what all variables you are going to use. Finally, you end up writing the code to the compiler. 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def add_two_numbers(arg1, arg2):
    print(f"The sum of the two numbers is {arg1+arg2}")

# The comma already introduces a space here. Wonder if it does this for string arguments too. It does. The other interesting thing - I've done all manners of positive and negative numbers here and this thing seems to hold the formatting between different variable types - strings with numbers, integers, float and so on
def subtract_two_numbers(arg1, arg2):
    print(f"The difference between the two numbers is {arg1 - arg2}")


# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)


# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print("We can even do math inside the parantheses:")
# cheese_and_crackers(10+20, 5+6)


# print("And we can combine the two, variables and math:")

# cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 20)

add_two_numbers (int(argv[1]), int(argv[2]))
# Can't subtract strings, no defined function, but addition will concatenate them
a = 98
b = 65
subtract_two_numbers(int(argv[1]), int(argv[2]))
subtract_two_numbers(49, int(argv[2]))
subtract_two_numbers(int(argv[1]), 36)
subtract_two_numbers(49, 36)
subtract_two_numbers(50 - 1, 40 - 10)
subtract_two_numbers(58 + 2, 40 - 10)
subtract_two_numbers(int(argv[1]) + 6, int(argv[2]) - 2)
subtract_two_numbers(int(argv[1]) - 8, int(argv[2]) - 20)
subtract_two_numbers(a, b)
subtract_two_numbers(a - 10, b + 19)
subtract_two_numbers(98.4, 23.2)