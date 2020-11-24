## exit(0) can be used to indicate a good exit, exit(1) or above can be used to indicate an error exit. This is not python specific, and can be consumed by the shell later on, which can use this to take further add error messages (or collect one from here)
from sys import exit
# The fucked up part here seems to be that you can only take 0 or 1 in gold, and anything else will get you to exit. The question I have - since the input is a string input, can 50 also be a valid input? Let's test. Hunch was correct 
def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# The bear room has a bear in front of the door - you can either open the door, and the bear does not move, or you can take the honey, or you can taunt the bear, or you just get from the compiler that it doesn't know what you mean. It's a two step process it seems - you taunt the bear and the bear moves, and then in the next step, you open the door and go to the gold room       
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
# Declaring a list here that houses all options, and putting it all in one place - wondering if that is a good idea? Should be, because it makes for easier readability
    choicelist = ["take honey", "taunt bear", "open door"]
    
    while True:
        choice = input("> ")
        
        if choice == choicelist[0]: # "take honey"
            dead("The bear looks at you then slaps your face off.")
        elif choice == choicelist[1] and not bear_moved: #"take honey" and bear_moved == False 
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == choicelist[1] and bear_moved: #"take honey" and bear_moved == True
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == choicelist[2] and bear_moved: #"open door" and bear_moved == True
            gold_room()
        else:
            print("I got no idea what that means.")
    
# The game inside the Cthulhu room - you can flee, and go back to the first room, or you can opt for head (how would the user know what to type?). Or you default back to the entry of the Cthulhu room
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()

# The dead() function basically just writes out a sarcastic "Good job" at the end of the statement with which it is called, and exits out of the execution

def dead(why):
    print(why, "Good job!")
    exit(0)

# The start function is a two door choice problem - either of the doors is taken, or the dead() function is invoked, which makes the program exit from everything

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# This function starts the entire program off

start()