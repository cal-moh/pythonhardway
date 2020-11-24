# Let's build a menu selector. The overall aim is to reduce the choice friction, and provide only one option at all times. Either this option works, or we move to the next. Philosophical question - how do you move out of infinite optionality? Write greater descriptors of what this option gives, or push user to qualify their choice? (Eventually)
# What day is it today? Depending on the day, I'll pick the default thing to eat. -- [Function] to find what day it is today, and what time it is right now
## Google style guide here - https://google.github.io/styleguide/pyguide.html#316-naming. Exceptions and ClassNames in camel case, GLOBAL_CONSTANTS in all caps. Everything else in underscores


import datetime
import random
## Resource for Datetime manipulations - https://www.w3schools.com/python/python_datetime.asp
# Why to make this as a separate function - is this repeatable code? No. Is this code that can be changed later? Probably. Wouldn't want to affect the rest of the code, hence modularised away

def day_and_time(): 
##PEP8 says functions and variables should be lowercase and separated by underscores
    current_datetime = datetime.datetime.now()
    current_day = current_datetime.strftime("%A")
    current_hour = current_datetime.strftime("%H")
    current_minute = current_datetime.strftime("%M")
    current_display_datetime = current_datetime.strftime("%c")
    return current_day, current_hour, current_minute, current_display_datetime



    
# Open CSV [Function to return today's lunch and dinner from CSV, depending on day and date as input (only dinner if lunch time is out)]. Global variables to define lunch time window and dinner time window
# Changing the return function to return entire list from which I will abstract all other items. Makes architecture extendable and doesn't impose restrictions other than CSV format on the file
def meal_plan(day):
    with open("mealplan.csv", "r") as f:
        lines = [line.rstrip('\n').split(',') for line in f]
    
    for line in lines:
        
        if line[0] == day:
            return line
        else:
            continue

# Test zone

# print(day, hour, minute, date)
# print(meal_plan(day))

day, hour, minute, date = day_and_time()
day, breakfast, lunch, dinner = meal_plan(day)
# I want to replace this while True with something else
satisfaction = False
while satisfaction == False:
    print("")
    print("Welcome to the All Consuming Decision for what to have today")
    print(f"The current date and time - {date}\n")
    print("The schedule for today reads: ")
    print(f"Lunch: {lunch}")
    print(f"Dinner: {dinner}\n")
# If this is the first pass at options, let it be lunch and dinner. If not, ask if lazy or exotic options are needed. Then, next     
    print("Are you good with these options (yes/no):")
    choice = input("> ")
    if choice == "yes":
        print("Enjoy your meal")
        satisfaction = True
    elif choice == "no":
        print("Do you want to see exotic options or lazy options (exotic/lazy)")
        choice2 = input("> ")
        if choice2 == "exotic":
            exotic_options = meal_plan("Exotic")
            print(f"Here's an exotic option : {exotic_options[random.randrange(1, len(exotic_options)-1, 1)]}")
            print("Are you satisfied with these options (yes/no)")
            choice3 = input("> ")
            if choice3 == "yes":
                print("Enjoy your meal")
                satisfaction = True                
            else:
                print("That's too bad. We'll try harder next time")
                satisfaction = True
        elif choice2 == "lazy":
            lazy_options = meal_plan("Lazy")
            print(f"Here's a lazy option : {lazy_options[random.randrange(1, len(lazy_options)-1, 1)]}")
            print("Are you satisfied with these options (yes/no)")
            choice3 = input("> ")
            if choice3 == "yes":
                print("Enjoy your meal")
                satisfaction = True                
            else:
                print("That's too bad. We'll try harder next time")
                satisfaction = True
        else:
            print("That's an invalid input. Starting again from the beginning")
    else:
        print("Please enter a valid input")
        continue
# If this is also not what the user feels like having, provide one of the weekend options. [Global variables to define weekend days]
# If this doesn't work, provide one of the exotic options, or fast cooking options

# The entire program must work on the command line but probably doesn't need any system inputs. So no need to import argv. I do need to import time library though. 



# Phase 2
# If that doesn't work, provide Zomato options

# In fact, at the outset, provide today's options, then provide lazy day options with different cuisines, and then provide zomato options in restaurants of choice

#If the user does not feel like eating this, I will build a different list of special case items to eat. If the user does not even feel like these, I will open up a series of options for them from Zomato or something? I think this is possible as the API is here - https://developers.zomato.com/documentation
