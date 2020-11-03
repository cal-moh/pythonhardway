from sys import argv
# I like this idea of assigning script every time to an argv zeroth argument, for it stops me from making any error because of an incorrect script name
script, filename = argv

print(f"We're going to erase {filename}.")
# Isn't there a way to handle this kind of Ctrl-C break with try-catch? Attempting this with the input() function
print("If you don't want that, hit CTRL=C (^C).")
print("If you do want that, hit RETURN.")

try: 
    input("?")
    print("Opening the file..")
    target = open(filename, 'w')
    # Interesting new function - truncate. I can also imagine there being some historical context to truncate, since the English meaning is clearly to stop, or cut off. Not to erase completely, which seems to be the meaning here.
    print("Truncating the file. Goodbye!")
    target.truncate()

    print("Now I'm going to ask you for three lines.")

    line1 = input("line1: ")
    line2 = input("line2: ")
    line3 = input("line3: ")

    print("I'm going to write these to the file.")

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print("And finally, we close it.")
    target.close()
except KeyboardInterrupt:
    print("Good call")
