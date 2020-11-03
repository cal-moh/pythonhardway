from sys import argv
# File name is obtained from the command line. The interesting part --> how do you set a default if someone doesn't give you a default extension? Failed for meta.txt vs meta. Second, how do you send a tab-tip sort of a thing?
script, filename = argv

# From docs, this file opens up in read mode by default (rt mode - read text, to be precise). The return is a "stream" - interesting, it's not a string, but a stream. 
# Differences between these - all are made from the abstract classes TextReader and TextWriter --> >StreamReader, StreamWriter (Conduits for bytes), StringReader and StringWriter (operate on arrays of characters), and BinaryReader and BinaryWriter (operate on arrays of bytes) https://www.c-sharpcorner.com/UploadFile/87b416/difference-between-text-stream-string-and-binary-data/

# So this can be opened up for reading as a list of lines, a big ass string, or even by characters. The conduit itself will have properties that allow you to open in certain kinds of modes, seek to a particular place, and so on. 

# From here -  https://docs.python.org/3/tutorial/inputoutput.html - opening up a file with binary in read/write mode will mess around with line endings and convert them to \n (can be \r\n or \n when input, but they are converted). Which means that for some other types of files like JPEGs, there's a chance that the file will get corrupted. So should be opened up only in binary mode. Also, files should be closed manually to free up system resources. Or they should be opened as -- with open('workfile') as f:
#    read_data = f.read()
txt = open(filename)

print(f"Here's your file {filename}:" )
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())