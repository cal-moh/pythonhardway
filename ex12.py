# I like the command pydoc. Gives me access to python documents.

# On Windows, this seems to work as "python -m pydoc <command>

# Reading about open(). I see a future where there is going to be a set of gotchas around encoding, mode in which the file is accessed. "w" is a dangerous mode, since this could kill the rest of the file. "x" for when a new file is to be created - error comes up whenever this file already exists. "r+b" opens up file without truncation. 

# Another gotcha for the future - the size of the buffer. I'd rather declare this explicitly if it is a self contained project, or I would default to the system buffer. I like the idea of declaring it at a project's end, because this is the sort of thing that extension to a new system in the future will fuck. Most files and compilers will use line buffering. 

# Opening in "b" mode results in byte objects rather than a file. I wonder if this is how you also end up passing and parsing byte arguments to and from the serial port. 

# There is built in error handling as well for encoding errors. This is something else that I would want to set as boilerplate for my teams. 

# I'm not sure what the meaning of file descriptor is, or the meaning of closefd. 

print("How old are you?", input())