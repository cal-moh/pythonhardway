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
    # w+ doesn't seem to open in append mode. Trying r+. r+ has the same problem. Will now attempt a+. Wonder why a+ and not a simply. So a+ creates a new file if it doesn't exist. r+ doesn't (and positions pointer at start of file to overwrite). a+ will open the file up for reading as well, a alone will open this up only for writing. w will create a file as well if none exists https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function 
    target = open(filename, 'a+')
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
