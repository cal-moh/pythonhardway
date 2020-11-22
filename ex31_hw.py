"""Writing a simple game to understand if-else loops.
The point of this game is to give the user choices between:
- Being a hunter
- Being a harvester"""

print("""Let's play the game of life in yet another form""")

# I plan to check hunter attributes and harvester attributes, and then compare the two. So essentially, three questions for hunter, three for harvester, but in a nested way.

print("Between the following options, which one do you prefer more?")
print("1. Meeting new people")
print("2. Working to build something")

choice1 = input("> ")

if choice1 == "1":
    print("What kind of new people do you like to meet?")
    print("1. People handling the business side")
    print("2. People handling the technical side")

    choice11 = input("> ")
    
    if choice11 == "1":
        print("Congratulations, you seem to be a hunter, in the hunter harvester paradigm")
    elif choice11 == "2":
        choice1 = "2" ##Changing a parent branch variable in the  middle of an if declaration will probably not make the parent branch shift happen
    
elif choice1 == "2":
    print("What kind of work do you like to handle?")
    print("1. Building tools")
    print("2. Running operations")
    
    choice21 = input("> ")
    
    if choice21 == "1":
        print("You're a builder. Unless you are great at what you do, you will either be commoditised. Even if you are great at what you do, you will be devalued.")
    elif choice21 == "2":
        print("Congratulations, you are a harvester.")
## There can only be one else for an if-elif-else set of statements. Also, an elif cannot just be replaced by an else if ():
else:
    print("No space for you in our paradigm. You are an outlier")