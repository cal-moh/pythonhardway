print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")
## It's probably better to structure code first and then write. In this, I think it is more helpful to use the group-by and minimise function as often as possible, especially when writing if-else statements, so that the global context visibility does not go away. 
if door == "1":
    # print("There's a giant bear here eating a cheese cake.")
    # print("What do you do?")
    # print("1. Take the cake.")
    # print("2. Scream at the bear.")
    # Can do this in the triple quote term as well, but it will break the indentation of the entire program. Unless I can find a way to suppress the tab character?
    print("""There's a giant bear here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.""")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job.")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
    
elif door == "2":
    print("You stare into the endless abyss of Ctulhu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")
    
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")