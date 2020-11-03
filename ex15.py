from sys import argv
# File name is obtained from the command line. The interesting part --> how do you set a default if someone doesn't give you a default extension? Failed for meta.txt vs meta. Second, how do you send a tab-tip sort of a thing?
script, filename = argv

# From docs, this file opens up in read mode by default (rt mode - read text, to be precise). The return is a "stream" - interesting, it's not a string, but a stream. 
# Differences between these - all are made from the abstract classes TextReader and TextWriter --> >StreamReader, StreamWriter (Conduits for bytes), StringReader and StringWriter (operate on arrays of characters), and BinaryReader and BinaryWriter (operate on arrays of bytes) https://www.c-sharpcorner.com/UploadFile/87b416/difference-between-text-stream-string-and-binary-data/
txt = open(filename)

print(f"Here's your file {filename}:" )
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())